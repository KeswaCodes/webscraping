import requests

url = 'https://vulavula-services.lelapa.ai/api/v1/entity_recognition/process'

# Headers
headers = {
    'Content-Type': 'application/json',
    'X-CLIENT-TOKEN': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjliYjQyYTI1Mjc5YjQ1Mjg5YmQ0ZTRmNjRiYzhhYzVmIiwiY2xpZW50X2lkIjoyOTcsInJlcXVlc3RzX3Blcl9taW51dGUiOjAsImxhc3RfcmVxdWVzdF90aW1lIjpudWxsfQ.jKXZGhPkqsqru1ladB2iOGb9cbF1eCrWkDJXva-6u6c' # Replace '<INSERT_TOKEN>' with your actual client token
}

# Request body
data = {
    "encoded_text": "Software engineering doctor physician dancer"
}

# Sending POST request
response = requests.post(url, headers=headers, json=data)

# Printing response
print(response.json())