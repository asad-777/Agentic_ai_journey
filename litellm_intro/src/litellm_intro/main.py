from litellm import completion  # type: ignore
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["GEMINI_API_KEY"] = os.getenv("API_KEY")


def main():
    response = completion(
        model="gemini/gemini-1.5-flash",
        messages=[{"content": "Hello, how are you?", "role": "user"}]
    )

    print(f"\n\n{response['choices'][0]['message']['content']}")


if __name__ == "__main__":
    main()
