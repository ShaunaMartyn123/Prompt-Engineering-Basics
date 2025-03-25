import pytest
from unittest.mock import patch, MagicMock
import os
from google import genai

def test_few_shot():
    #Test the api key - Instead of getting the api key from .env it gets fake_api_key
    with patch("os.getenv", return_value="fake_api_key"), \
         patch ("google.genai.Client", autospec=True) as MockClient:

        mock_client = MockClient.return_value
        mock_client.models.generate_content.return_value = MagicMock(text="Mocked response")

        client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY")) 
        
        # Test the prompt
        for few_shot_prompt in [""
        "Question: You can use it to listen to music and you put it over your ears. "
        "Answer: Headphones"
        "Example 2:"
        "Question:  It is has 2 straps and is used to carry books on your back."
        "Answer: Backpack"
        "Example 3: Q"
        "Question: It is used to tell time and is worn on the wrist"
        "Answer: "]:
             assert client.models.generate_content(model="gemini-2.0-flash", contents=few_shot_prompt).text == "Mocked response"
