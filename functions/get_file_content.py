import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    
    working_dir_abs = os.path.abspath(working_directory)
    file_dir_abs = os.path.abspath(os.path.join(working_directory, file_path))
    valid_target_dir = os.path.commonpath([working_dir_abs, file_dir_abs]) == working_dir_abs

    if not valid_target_dir:

        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(file_dir_abs):

        return f'Error: File not found or is not a regular file: "{file_path}"'

    content = ''

    try:
        with open(file_dir_abs, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
    except Exception as e:

        return f"Error: {e}"

    if not content:
        return file_content_string
    return content
