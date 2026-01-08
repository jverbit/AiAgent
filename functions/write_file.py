import os

def write_file(working_directory, file_path, content):
    
    working_dir_abs = os.path.abspath(working_directory)
    file_dir_abs = os.path.abspath(os.path.join(working_directory, file_path))
    valid_target_dir = os.path.commonpath([working_dir_abs, file_dir_abs]) == working_dir_abs

    if not valid_target_dir:

        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if os.path.isdir(file_dir_abs):

        return f'Error: Cannot write to "{file_path}" as it is a directory'
    os.makedirs(working_directory, exist_ok=True)

    try:
        with open(file_dir_abs, "w") as f:
            f.write(content)

            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:

        return f"Error: {e}"
