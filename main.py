import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def main():
    print("Hello from bootdevaiagent!")
    if not api_key:
        raise RuntimeError("Error: api_key wasn't found in .env")

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    
    for _ in range(5):
        response = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions], 
                system_instruction=system_prompt,
                temperature=0
                )
        )
        if not response.usage_metadata:
            raise RuntimeError("Error: response contained no metadata")
        if response.candidates:
            for candidate in response.candidates:
                if candidate.content:
                    messages.append(candidate.content)
        if not response.function_calls:
            print("Final response:")
            print(response.text)
            return
        function_responses = []
        for function_call in response.function_calls:
            result = call_function(function_call, args.verbose)
            function_responses.append(result.parts[0])
        messages.append(types.Content(role="user", parts=function_responses))
    print("Agent did not reach a final response within 5 iterations")
    
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
