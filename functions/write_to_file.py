import os

def write_file(working_directory, file_path, content):
    full_path = os.path.join(working_directory, file_path)
    
    abs_curr = os.path.realpath(working_directory)
    abs_file = os.path.realpath(full_path)

    common_path = os.path.commonpath((abs_curr, abs_file))

    if common_path != abs_curr:
        return  f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    elif not os.path.exists(os.path.dirname(full_path)):
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

    try:
        file_content = write_to(full_path, content)
    except Exception as e:
        return f"Error: {str(e)}"

    return file_content

def write_to(file_path, content):
    num_written = 0
    with open(file_path, "w") as f:
        num_written = f.write(content)

    if num_written > 0:
        return f'Successfully wrote to "{file_path}" {len(content)} characters written'
    else:
        raise Exception("Invalid argument")
        
