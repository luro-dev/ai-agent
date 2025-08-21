from google import genai
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_to_file import write_file
from functions.run_python_file import run_python_file 
from google.genai import types

def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    function_map = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "write_file": write_file,
        "run_python_file": run_python_file,
    }
    
    if function_call_part.name not in function_map:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Unknown function: {function_call_part.name}"}
                )
            ]
        )

    function_name = function_call_part.name
    args = dict(function_call_part.args)
    args["working_directory"] = "./calculator"
    actual_function = function_map[function_name]
    result = actual_function(**args)

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": result}
            )
        ]
    )
