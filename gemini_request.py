from google import genai

# Initialize Gemini client with API Key
client = genai.Client(api_key="AIzaSyBh5dES-rcu14U8DWCJIxKbx0mKhjrA1l0")   

# Define different prompting techniques
prompts = {
    "Zero-Shot": "What is the capital of France?",
    
    "Few-Shot": "The capital of Germany is Berlin. The capital of Spain is Madrid. What is the capital of France?",
    
    "Chain-of-Thought": """To find the capital of France, follow these steps:
        1. Identify France as a country in Europe.
        2. Look at major cities in France.
        3. The capital city is the political and economic center.
        4. Based on this, what is the capital of France?"""
}

# Define open-ended and closed-ended questions
questions = {
    "open_ended": "what is the capital of Spain?",
    "closed_ended": "Is Paris the capital of France?"
}

# Function to get response from Gemini
def get_response(question):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=question
    )
    return response.text  # Extract response text

# Store all results for documentation
findings = "## Gemini AI Prompting & Question Type Analysis\n\n"

# Test different prompting techniques
findings += "### 1️⃣ Prompting Techniques\n\n"
for prompt_type, prompt_text in prompts.items():
    response_text = get_response(prompt_text)
    findings += f"**{prompt_type} Prompt:**\n{prompt_text}\n\n**Response:**\n{response_text}\n\n{'='*80}\n\n"
    print(f"\n--- {prompt_type} Prompt ---\n")
    print(response_text)
    print("\n" + "="*80)

# Test open-ended vs. closed-ended questions
findings += "### 2️⃣ Open-Ended vs. Closed-Ended Questions\n\n"

open_response = get_response(questions["open_ended"])
closed_response = get_response(questions["closed_ended"])

findings += f"**🔹 Open-Ended Question:** {questions['open_ended']}\n\n**Response:**\n{open_response}\n\n"
findings += f"**🔹 Closed-Ended Question:** {questions['closed_ended']}\n\n**Response:**\n{closed_response}\n\n"

# Print Open-Ended vs. Closed-Ended Question Responses
print("\n🔹 Open-Ended Question:")
print(f"Q: {questions['open_ended']}\nA: {open_response}\n")

print("\n🔹 Closed-Ended Question:")
print(f"Q: {questions['closed_ended']}\nA: {closed_response}\n")

# Save findings to a text file
with open("findings.txt", "w", encoding="utf-8") as file:
    file.write(findings)

print("\n✅ Findings have been documented in 'findings.txt'.")
