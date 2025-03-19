from google import genai
from dotenv import load_dotenv
import os 


# Load environment variables from .env
load_dotenv()

# Retrieve the API key
api_key = os.getenv("GOOGLE_API_KEY")

# Initialize the Gemini API client
client = genai.Client(api_key=api_key)

#Using a list to store prompts - Zero Shot - Can add 1 or multiple questions here
prompts = [
    "What is the capital of Spain?",
    "What is the capital of France?",
    "What is the capital of Scotland?"
    
]

#Loop through each prompt and send it separately
for prompt in prompts:
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )

    #Print the question and the response
    print(f"Prompt: {prompt}")
    print(f"Response: {response.text}")
