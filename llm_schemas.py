from google import genai
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
        required=["directory"],
    ),
)

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads files in the specified directory, constrained to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The filepath to the file we want to read relative to the working directory"
            )
        },
        required=["file_path"],
    )
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs files in the specified directory with the option to execute files with optional arguments, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The filepath to run the file from, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description= "Optional command-line arguments to pass to the Python script."
            )
        },
        required=["file_path"],
    ),
)

schema_write_to_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes to a file in the specified directory, constrained to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The filepath to the file we want to write to relative to the working directory"
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the specified file"
            )
        },
        required=["file_path", "content"],
    )
)

