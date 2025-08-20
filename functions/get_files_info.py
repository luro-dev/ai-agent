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

    return directory_contents(full_path)



# os.path.getsize 
# os.path.isfile
# os.listdir


def directory_contents(directory_path):
    content_container = os.listdir(directory_path)
    print(content_container) 

