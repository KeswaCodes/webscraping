
# Endpoint URL
import requests
url = 'https://vulavula-services.lelapa.ai/api/v1/translate/process'

# Headers
headers = {
    'Content-Type': 'application/json',
    'X-CLIENT-TOKEN': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjAwNTFkODM4MDI0ZDRlMTdhN2YzNmI2MWI4ZDA5YTYwIiwiY2xpZW50X2lkIjoyOTIsInJlcXVlc3RzX3Blcl9taW51dGUiOjAsImxhc3RfcmVxdWVzdF90aW1lIjpudWxsfQ.QdISkHBNZaQIRjB0fufteJ24hJkuW1j06bfJLQxpn2g' # Replace '<INSERT_TOKEN>' with your actual client token
}

# Request body
data = {
  "input_text": """ Welcome

Before we go ahead, we would love to get to know you a little better.

What is your name?""",
  "source_lang": "eng_Latn",
  "target_lang": "zul_Latn"
}

# Sending POST request
response = requests.post(url, headers=headers, json=data)

# Printing response
print(response.json())






# Welcome 🥳

# Before we go ahead, we would love to get to know you a little better.

# What is your name?