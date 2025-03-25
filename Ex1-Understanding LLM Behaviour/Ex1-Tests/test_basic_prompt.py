import pytest
from unittest.mock import patch, MagicMock
import os
from google import genai

def test_gemini_api():
    #Test the api key - Instead of getting the api key from .env it gets fake_api_key
    with patch("os.getenv", return_value="fake_api_key"), \
         patch ("google.genai.Client", autospec=True) as MockClient:

        mock_client = MockClient.return_value
        mock_client.models.generate_content.return_value = MagicMock(text="Mocked response")

        client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY")) 

        # Test the prompt 
        for prompt in ["What is the capital of Spain?", "What is the capital of France?", "What is the capital of Scotland?"]:
             assert client.models.generate_content(model="gemini-2.0-flash", contents=prompt).text == "Mocked response"
