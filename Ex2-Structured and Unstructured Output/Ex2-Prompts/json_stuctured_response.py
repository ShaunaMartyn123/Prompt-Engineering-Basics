from google import genai
from dotenv import load_dotenv
import os 


# Load environment variables from .env
load_dotenv()

# Retrieve the API key
api_key = os.getenv("GOOGLE_API_KEY")

# Initialise the Gemini API client
client = genai.Client(api_key=api_key)

expected_json_example =  """
    The response should strictly follow this JSON format:
    {
        "question" : "What is the capital of Germany?",
        "answer" : "Your answer goes here",
        "confidence" : "High/Medium/Low"
    }
    """

# Prompts  - Zero shot
prompts = f"""

        Now answer the following questions:

        "In what year did the Titanic sink?"
        "List the 7 wonders of the world"
        "How long is the great wall of China?"
        "Is Barcelona the capital of Spain?"

        {expected_json_example}
        
    """

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents = prompts
)

# Print the question and the response
print(f"Prompt: {prompts}")
print(f"Response: {response.text}")


