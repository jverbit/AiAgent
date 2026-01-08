from functions.get_file_content import get_file_content

def print_block(label, result, indent="  "):
    print(label)
    for line in result.splitlines():
        print(f"{indent}{line}")

result = get_file_content("calculator", "lorem.txt")
print_block("Result for 'lorem.txt' in calculator directory:", result, indent="  ")

result = get_file_content("calculator", "main.py")
print_block("Result for 'main.py' in calculator directory:", result, indent="  ")

result = get_file_content("calculator", "pkg/calculator.py")
print_block("Result for 'pkg/calculator.py' in calculator directory:", result, indent="  ")

result = get_file_content("calculator", "/bin/cat")
print_block("Result for '/bin/cat' in calculator directory:", result, indent="    ")

result = get_file_content("calculator", "pkg/does_not_exist.py")
print_block("Result for 'pkg/does_not_exist.py' in calculator directory:", result, indent="    ")