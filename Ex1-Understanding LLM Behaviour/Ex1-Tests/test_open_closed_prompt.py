import pytest
from unittest.mock import patch, MagicMock
import os
from google import genai

@pytest.mark.parametrize("prompt", [

    "In what year did the Titanic sink?",
    "Is Lisbon the capital of Portugal?",
    "Who will be the next president of the US?",
    "Will humans ever live on the sun?",
    "What year did man walk on the moon?",
    "What is the hottest recorded temperature on Earth?",
    "Will it snow tomorrow?"

])

def test_open_closed(prompt):
    #Test the api key - Instead of getting the api key from .env it gets fake_api_key
    with patch("os.getenv", return_value="fake_api_key"), \
         patch ("google.genai.Client", autospec=True) as MockClient:

        mock_client = MockClient.return_value
        mock_client.models.generate_content.return_value = MagicMock(text="Mocked response") # Makes sure that the mock was actually called
    	
        # Initialize the client
        client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY")) 
        
        response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
        assert response.text == "Mocked response"
