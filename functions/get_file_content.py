import os

def get_file_content(working_directory, file_path):
    full_path = os.path.join(working_directory, file_path)

    abs_curr = os.path.realpath(working_directory)
    abs_file = os.path.realpath(full_path)

    common_path = os.path.commonpath((abs_curr, abs_file))

    if common_path != abs_curr:
       return  f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file):
       return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        file_content = read_file_content(full_path)
    except Exception as e:
        return f"Error: {str(e)}"

    return file_content

def read_file_content(filepath):
    MAX_CHARS = 10000
    
    file_size = os.path.getsize(filepath)

    with open(filepath, "r") as f:
        file_content_string = f.read(MAX_CHARS)
    
    if file_size > 10_000:
        file_content_string += f'[...File "{filepath}" truncated at 10000 characters]'
    
    return file_content_string



