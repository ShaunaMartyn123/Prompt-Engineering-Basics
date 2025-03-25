import pytest
from unittest.mock import patch, MagicMock
import os
from google import genai
import json

"""
Test 1. Testing for API key 
Test 2. The test mocks genai.Client to prevent a real API call.
Test 3. The test mocks the call to Gemini and returns "Mocked response" - avoiding real API requests.
Test 4. The response follows the correct JSON format. 

"""

@pytest.mark.parametrize("prompt_list", [

    "In what year did the Berlin wall fall?",
    "Who invented the internet?",
    "Did Tim Berners-Lee invent the internet?",
    "Who invented the World Wide Web?"
    "Who published the first English Dictionary?"
    "Will Donald Trump be the next US president?"
])

def test_few_shot(prompt_list):
    # Test the API response with a few-shot learning prompt.
    # Test the api key - Instead of getting the api key from .env it gets fake_api_key
    with patch("os.getenv", return_value="fake_api_key"), \
         patch ("google.genai.Client", autospec=True) as MockClient:

        mock_client = MockClient.return_value
        mock_client.models.generate_content.return_value = MagicMock(text=json.dumps({
            "question":"Sample Question",
            "answer": "Sample Answer",
            "confidence": "High"
        }))

        client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY")) 

        # Convert list to formatted string
        formatted_prompts = "\n".join(f'"{q}"' for q in prompt_list)

        prompt_text = f"""
        
            Expect JSON format:
            {{
                 "question":"What is the capital of Germany?",
                "answer": "Your answer goes here",
                "confidence": "High/Medium/Low"
            }}

            Now answer the following questions in a strict JSON format:
            {formatted_prompts}
        """

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt_text
        ).text

        # Validate response in JSON 
        try: 
            response_json = json.loads(response)
            assert isinstance(response_json, dict)
            assert "question" in response_json
            assert "answer" in response_json
            assert "confidence" in response_json
        except json.JSONDecodeError: 
            pytest.fail("Response is not valid JSON")




