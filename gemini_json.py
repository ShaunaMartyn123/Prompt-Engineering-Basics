from google import genai
import json  # Import JSON module

# Initialize Gemini client
client = genai.Client(api_key="ADD GOOGLE AI STUDIO API KEY HERE ")  

# Define a structured prompt
prompts = {
    "Zero-Shot":"""
    Provide the following details in JSON format:
    {
        "question": "What is the capital of France?",
        "answer": "Your answer here",
        "confidence": "How confident are you in this answer? (High/Medium/Low)"
    }
    """,

    "Few-Shot": """
        Here are some examples of countries and their capitals:
        - The capital of Germany is Berlin.
        - The capital of Spain is Barcelona

        Now provide the following details in JSON format:
        {
            "question" : "What is the capital of France",
            "answer" : "Your answer here",
            "confidence" : "How confident are youn in this answer? (High/Medium/Low)"
        
        }
    """,

    "Chain-of-Thought" : """
    To determine the capital of France
    1. Identify France as a country in Europe.
    2. Look at the major cities in France.
    3. The capital city is the political and economic center.
    4. Based on this what is the capital of France?

    Now provide the following details in JSON format:
    {
        "question" : "What is the capital of France?",
        "answer" : "Your answer here",
        "confidence" : "How confident are you in this answer? (High/Medium/Low)"
    }
    """
}

# Function to get a structured response
def get_json_response(prompt):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return response.text  # Extract response text

for prompt_type, prompt_text in prompts.items():
    print(f"\n--- {prompt_type} Prompt ---\n")
    json_response = get_json_response(prompt_text) # Get response from Gemini

    # Try to parse the response as JSON
    try:
        # Directly print the response as it is JSON-like
        parsed_response = json.loads(json_response)  # Attempt to parse as JSON
        print("\n🔹 Structured JSON Output:")
        print(json.dumps(parsed_response, indent=4))  # Pretty-print JSON
    except json.JSONDecodeError:
        # If not JSON, print the raw response
        print("\n⚠️ Error: Response is not valid JSON. Here is the raw output:")
        print(json_response)  # Print the raw response as it is
    print("\n" + "="*80)
