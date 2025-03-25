# Modify the prompt to enforce consistent formatting across multiple queries.
# Hint: Provide an explicit example of the expected JSON structure.

from google import genai
from dotenv import load_dotenv
import os 
import json


# Load environment variables from .env
load_dotenv()

# Retrieve the API key
api_key = os.getenv("GOOGLE_API_KEY")

# Initialize the Gemini API client
client = genai.Client(api_key=api_key)

expected_json_example =  """
    The response should strictly follow this JSON format:
    {
        "question" : "What is the capital of Germany?",
        "answer" : "Your answer goes here",
        "confidence" : "High/Medium/Low"
    }
    """

# Convert to JSON format for consistent formatting 
json_example_string = json.dumps(expected_json_example, indent=4)

# Prompts  - Zero shot
prompts = f"""

        Expected JSON format:
        {json_example_string}

        Now answer the following questions in a strict JSON format:

        "In what year did the Berlin wall fall?",
        "Who invented the internet?",
        "Did Tim Berners-Lee invent the internet?",
        "Who invented the World Wide Web?"
        "Who published the first English Dictionary?"
        "Will Donald Trump be the next US president?"
                
    """

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents = prompts
)

# Print the question and the response
print(f"Prompt: {prompts}")
print(f"Response: {response.text}")


