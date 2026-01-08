from functions.write_file import write_file

def print_block(label, result, indent="  "):
    print(label)
    for line in result.splitlines():
        print(f"{indent}{line}")

result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
print_block("Result for 'lorem.txt' in calculator directory:", result, indent="  ")

result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
print_block("Result for 'lorem.txt' in calculator directory:", result, indent="  ")

result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
print_block("Result for 'lorem.txt' in calculator directory:", result, indent="    ")
