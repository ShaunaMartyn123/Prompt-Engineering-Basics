import pytest
from unittest.mock import patch, Mock
import os
from google import genai
import json

"""
Test 1. Ensures the API key is retrieved correctly.
Test 2. Mocks `genai.Client` to prevent real API calls.
Test 3. Mocks API responses to return fake data instead of real API requests.
Test 4. Validates that the response follows the expected JSON format.
"""

@pytest.mark.parametrize("prompt_list", [
    [
        "In what year did the Titanic sink?",
        "List the 7 wonders of the world",
        "How long is the Great Wall of China?",
        "Is Barcelona the capital of Spain?"
    ]
])
def test_few_shot(prompt_list):
    # Mock the API key retrieval
    with patch("os.getenv", return_value="fake_api_key"), \
         patch("google.genai.Client", autospec=True) as MockClient:

        mock_client = MockClient.return_value
        mock_client.models.generate_content.return_value = Mock(text=json.dumps({
            "question": "Sample Question",
            "answer": "Sample Answer",
            "confidence": "High"
        }))

        client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

        # Convert list to formatted string
        formatted_prompts = "\n".join(f'"{q}"' for q in prompt_list)

        prompt_text = f"""
            Expect JSON format:
            {{
                "question": "What is the capital of Germany?",
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

        # Validate response is proper JSON
        try:
            response_json = json.loads(response)
        except json.JSONDecodeError:
            pytest.fail("Response is not valid JSON")

        assert isinstance(response_json, dict), "Response should be a dictionary"
        assert "question" in response_json, "Missing 'question' field in response"
        assert "answer" in response_json, "Missing 'answer' field in response"
        assert "confidence" in response_json, "Missing 'confidence' field in response"

        # Validate JSON values
        assert isinstance(response_json["question"], str) and response_json["question"].strip(), "Invalid 'question' value"
        assert isinstance(response_json["answer"], str) and response_json["answer"].strip(), "Invalid 'answer' value"
        assert response_json["confidence"] in ["High", "Medium", "Low"], "Invalid 'confidence' value"
