import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from llm_schemas import *
from functions.call_function import call_function

def main():
    # Loading variables from .env,
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    # Creating new instance of Gemini client
    client = genai.Client(api_key=api_key)
    
    # Checks for no conent provided
    try:
        user_prompt = sys.argv[1]
    except IndexError:
        sys.exit(1)
    
    if user_prompt == "":
        sys.exit(1)

    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories
    - Read file contents
    - Execute Python files with optional arguments
    - Write or overwrite files

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_write_to_file,
            schema_run_python_file,
        ]
    )
    # Keep prompts as a list to play a role in the conversation
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    

    # Getting response from client
     
    for i in range(0, 20):
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash-001",
                contents=messages,
                config=types.GenerateContentConfig(
                    tools=[available_functions],
                    system_instruction=system_prompt),
            )

            for res in response.candidates:
                messages.append(res.content)

            if not response.function_calls:
                print(response.text)
                break

            for func in response.function_calls:
                verbose = True if "--verbose" in sys.argv else False
                types_content = call_function(func, verbose)
                messages.append(types_content)

                if not types_content.parts or not types_content.parts[0].function_response:
                    raise Exception("empty function call result")

                response_data = types_content.parts[0].function_response.response
                if verbose:
                    print(f"-> {response_data}")
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
