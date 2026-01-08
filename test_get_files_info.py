from functions.get_files_info import get_files_info

def print_block(label, result, indent="  "):
    print(label)
    for line in result.splitlines():
        print(f"{indent}{line}")

# 1) current directory
result = get_files_info("calculator", ".")
print_block("Result for current directory:", result, indent="  ")

# 2) 'pkg' directory
result = get_files_info("calculator", "pkg")
print_block("Result for 'pkg' directory:", result, indent="  ")

# 3) '/bin' directory
result = get_files_info("calculator", "/bin")
print_block("Result for '/bin' directory:", result, indent="    ")

# 4) '../' directory
result = get_files_info("calculator", "../")
print_block("Result for '../' directory:", result, indent="    ")