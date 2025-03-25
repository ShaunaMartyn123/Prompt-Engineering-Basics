from google import genai
from dotenv import load_dotenv
import os 


# Load environment variables from .env
load_dotenv()

# Retrieve the API key
api_key = os.getenv("GOOGLE_API_KEY")

# Initialize the Gemini API client
client = genai.Client(api_key=api_key)

# Chain of Thought prompts
chain_of_thought_prompt = """
    
    Q: John has 3 packets of stickers. Each packet has 10 stickers. He buys 2 more packets. How many stickers does he have now?
    A: He started with 30 stickers. 2 packets with 10 stickers each is 20. 30 + 20 = 50. The answer is 50.

    Q: Mary has 5 apples. She gave 2 to her friend and then she bought 4 more. How many apples does Mary have now?
    
"""

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents = chain_of_thought_prompt
)

#Print the question and the response
print(f"Prompt: {chain_of_thought_prompt}")
print(f"Response: {response.text}")
