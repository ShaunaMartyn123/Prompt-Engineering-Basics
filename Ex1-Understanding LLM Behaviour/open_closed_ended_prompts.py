from google import genai
from dotenv import load_dotenv
import os 


# Load environment variables from .env
load_dotenv()

# Retrieve the API key
api_key = os.getenv("GOOGLE_API_KEY")

# Initialize the Gemini API client
client = genai.Client(api_key=api_key)

# Opend and closed ended prompt mix of example questions
open_closed_ended_prompts = """

    Answer the following questions then classify wheather they are "open-ended" or "closed-ended":

    1. In what year did the Titanic sink?,
    2. Is Lisbon the capital of Portugal?
    3. Who will be the next president of the US?
    4. Will humans ever live on the sun?
    5. What year did man walk on the moon?
    6. What is the hottest recorded temperature on Earth?
    7. Will it snow tomorrow?
    """

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents = open_closed_ended_prompts
)

#Print the question and the response
print(f"Prompt: {open_closed_ended_prompts}")
print(f"Response: {response.text}")


