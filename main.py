import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from llm_schemas import *

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
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt),
    )
    
    # Handle verbose flag --verbose (give more info)
    if "--verbose" in sys.argv:
        print(f"User prompt: {user_prompt}\nPrompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}")
    elif response.function_calls:
        for func in response.function_calls:
            print(f"Calling function: {func.name}({func.args})")
    else:
        print(response.text)
        

if __name__ == "__main__":
    main()
