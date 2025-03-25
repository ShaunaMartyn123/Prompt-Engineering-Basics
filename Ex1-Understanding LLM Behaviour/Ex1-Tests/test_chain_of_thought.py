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
        for chain_of_thought_prompt in ["""
    
            Q: John has 3 packets of stickers. Each packet has 10 stickers. He buys 2 more packets. How many stickers does he have now?
            A: He started with 30 stickers. 2 packets with 10 stickers each is 20. 30 + 20 = 50. The answer is 50.

            Q: Mary has 5 apples. She gave 2 to her friend and then she bought 4 more. How many apples does Mary have now?
        
        """]:
             assert client.models.generate_content(model="gemini-2.0-flash", contents=chain_of_thought_prompt).text == "Mocked response"
