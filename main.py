import os
from dotenv import load_dotenvi
from google import genai

def main():
    # Loading variables from .env,
    load_dotenvi()
    api_key = os.environ.get("GEMINI_API_KEY")

    # Creating new instance of Gemini client
    client = genai.Client(api_key=api_key)
    content = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

    # Getting response from client
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=content
    )

    print(response.text)


if __name__ == "__main__":
    main()
