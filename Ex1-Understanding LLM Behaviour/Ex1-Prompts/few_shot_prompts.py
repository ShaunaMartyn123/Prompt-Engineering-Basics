from google import genai
from dotenv import load_dotenv
import os 

# Load environment variables from .env
load_dotenv()

# Retrieve the API key
api_key = os.getenv("GOOGLE_API_KEY")

# Initialize the Gemini API client
client = genai.Client(api_key=api_key)

#Using a list to store prompts - Few-Shot prompts
few_shot_prompt = """
    
    Guess the object based on its description

    Example 1:
    Question: You can use it to listen to music and you put it over your ears.
    Answer: Headphones

    Example 2:
    Question:  It is has 2 straps and is used to carry books on your back.
    Answer: Backpack

    Example 3: 
    Question: It is used to tell time and is worn on the wrist
    Answer: 
    
"""

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents = few_shot_prompt
)

#Print the question and the response
print(f"Prompt: {few_shot_prompt}")
print(f"Response: {response.text}")
