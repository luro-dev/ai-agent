import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)

    target_abs_path = os.path.realpath(full_path)
    working_dir_abs_path = os.path.realpath(working_directory)
    common_path = os.path.commonpath([working_dir_abs_path, target_abs_path])

    # test longest common path to see if they are the same
    if common_path != working_dir_abs_path:
        return f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory"
    elif not os.path.isdir(target_abs_path):
        return f"Error: \"{directory}\" is not a directory"
    
    try:
        files_info = directory_contents(full_path)
    except Exception as e:
        return f"Error: {str(e)}"

    if directory == ".":
        return f"Result for current directory:\n{files_info}"
    else:
        return f"Result for '{directory}' directory:\n{files_info}"





# os.path.getsize 
# os.path.isfile
# os.listdir


def directory_contents(directory_path):
    content_container = os.listdir(directory_path)
    
    # Loop through formatting string
    for i in range(len(content_container)):
        item_name = content_container[i]
        item_path = os.path.join(directory_path, item_name)
        item_size = os.path.getsize(item_path)
        is_dir = os.path.isdir(item_path)
        content_container[i] = f"- {item_name}: file_size={item_size} bytes, is_dir={is_dir}"
    return "\n".join(content_container)

