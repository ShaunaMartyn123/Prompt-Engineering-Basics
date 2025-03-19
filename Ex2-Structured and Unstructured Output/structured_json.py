from google import genai
from dotenv import load_dotenv
import os 


# Load environment variables from .env
load_dotenv()

# Retrieve the API key
api_key = os.getenv("GOOGLE_API_KEY")


# Define a structured prompt 
expected_json_example = """
    The response should strictly follow this JSON format:
    {
        "question" : "What is the capital of France",
        "answer" : "Your answer here",
        "confidence" : "High/Medium/Low"

    }
    """

# Define a structured prompt
prompts = {
    "Zero-Shot": f"""
    {expected_json_example}

    Now provide the asnwer for the following question:
    "What is the capital of France?"
    """,

    "Few-Shot": f"""
        Here are some examples of countries and their capitals:
        - The capital of Germany is Berlin.
        - The capital of Spain is Madrid.
    
    {expected_json_example}

    """,

    "Chain-of-Thought" : f"""
    To determine the capital of France
    1. Identify France as a country in Europe.
    2. Look at the major cities in France.
    3. The capital city is the political and economic center.
    4. Based on this what is the capital of France?

    {expected_json_example}

    Now provide the answer for the following question:
    "What is the capital of France?"
    """
}

def clean_json_response(response_text):
    cleaned_text = re.sub(r"```json\s*|\s*```", "", response_text.strip())
    return cleaned_text

# Function to get a structured response
def get_json_response(prompt):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return response.text  # Extract response text

for prompt_type, prompt_text in prompts.items():
    print(f"\n--- {prompt_type} Prompt ---\n")
    raw_response = get_json_response(prompt_text)  # Get response from Gemini
    cleaned_response = clean_json_response(raw_response)  # Cleanup response

    # Try to parse the response as JSON
    try:
        # Directly print the response as it is JSON-like
        parsed_response = json.loads(cleaned_response)  # Attempt to parse as JSON
        print("\n🔹 Structured JSON Output:")
        print(json.dumps(parsed_response, indent=4))  # Pretty-print JSON
    except json.JSONDecodeError:
        # If not JSON, print the raw response
        print("\n⚠️ Error: Response is not valid JSON. Here is the raw output:")
        print(cleaned_response)  # Print the raw response as it is
    print("\n" + "="*80)
