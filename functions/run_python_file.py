import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    full_path = os.path.join(working_directory, file_path)

    abs_curr = os.path.realpath(working_directory)
    abs_file = os.path.realpath(full_path)

    common_path = os.path.commonpath((abs_curr, abs_file))

    if common_path != abs_curr:
       return  f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file):
       return f'Error: File "{file_path}" not found.'
    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        run_object_str = run_file(full_path, args)
    except Exception as e:
        return f"Error: executing Python file: {e}"

    return run_object_str
    
#Set a timeout of 30 seconds to prevent infinite execution
#Capture both stdout and stderr
#Set the working directory properly
#Pass along the additional args if provided
def run_file(full_path, args, **kwargs):
    cmd = ["python3", full_path] + args
    run_obj = subprocess.run(cmd, capture_output=True, timeout=30, text=True, **kwargs)
    exit_code = run_obj.returncode
    output = "No output produced" if run_obj.stdout == "" else run_obj.stdout
    result = (
    f"STDOUT: {output}\n"
    f"STDERR: {run_obj.stderr}\n"
    )

    if exit_code != 0:
        result += f"Process exited with code {exit_code}\n"

    return result
