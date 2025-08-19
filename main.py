import os
from dotenv import load_dotenv
from google import genai

def main():
    # Loading variables from .env,
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    # Creating new instance of Gemini client
    client = genai.Client(api_key=api_key)
    content = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

    # Getting response from client
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=content
    )

    # Printing the prompt response and token usage 
    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}\n Response tokens: {reponse.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
