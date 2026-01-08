import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    
    working_dir_abs = os.path.abspath(working_directory)
    file_dir_abs = os.path.abspath(os.path.join(working_directory, file_path))
    valid_target_dir = os.path.commonpath([working_dir_abs, file_dir_abs]) == working_dir_abs

    if not valid_target_dir:

        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(file_dir_abs):

        return f'Error: "{file_path}" does not exist or is not a regular file'
    if not file_path.endswith(".py"):

        return f'Error: "{file_path}" is not a Python file'

    try:
        command = ["python", file_dir_abs]
        if args:
            command.extend(args)
        completed = subprocess.run(command, cwd=working_dir_abs, capture_output=True, timeout=30, text=True)
        
        if completed.returncode != 0:

            return f'Process exited with code {completed.returncode}'
        if not completed.stdout and not completed.stderr:

            return 'No output produced'

        output_string = ''
        if completed.stdout:
            output_string = f'STDOUT: {completed.stdout}'
        if completed.stderr:
            output_string = output_string + f'STDERR: {completed.stderr}'

        return output_string

    except Exception as e:

        return f"Error: executing Python file: {e}"
    