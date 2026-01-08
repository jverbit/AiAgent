from functions.run_python_file import run_python_file

def print_block(label, result, indent="  "):
    print(label)
    for line in result.splitlines():
        print(f"{indent}{line}")

result = run_python_file("calculator", "main.py")
print_block("Result for 'main.py' in calculator directory:", result, indent="  ")

result = run_python_file("calculator", "main.py", ["3 + 5"])
print_block("Result for 'main.py' inputting [ 3 + 5 ] in calculator directory:", result, indent="  ")

result = run_python_file("calculator", "tests.py")
print_block("Result for 'tests.py' in calculator directory:", result, indent="    ")

result = run_python_file("calculator", "../main.py")
print_block("Result for '../main.py' in calculator directory:", result, indent="    ")

result = run_python_file("calculator", "nonexistent.py")
print_block("Result for 'nonexistent.py' in calculator directory:", result, indent="    ")

result = run_python_file("calculator", "lorem.txt")
print_block("Result for 'lorem.txt' in calculator directory:", result, indent="    ")
