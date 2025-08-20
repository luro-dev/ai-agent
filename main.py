import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

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

    # Keep prompts as a list to play a role in the conversation
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]


    # Getting response from client
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages
    )
    
    # Handle verbose flag --verbose (give more info)
    if "--verbose" in sys.argv:
        print(f"User prompt: {user_prompt}\nPrompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}")
    else:
        print(response.text)

if __name__ == "__main__":
    main()
