# Lab 17 - Quotes API
import requests
import json

# Get random quote
response = requests.get('https://favqs.com/api/qotd')

# Parse JSON message
message = json.loads(response.text)

# Display to user
print(f'"{message["quote"]["body"]}" - by {message["quote"]["author"]}')