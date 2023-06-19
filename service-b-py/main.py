import json
from googlefinance import getQuotes

# Get the stock prices from the Google Finance API.
alphabet_response = json.dumps(getQuotes('GOOG'), indent=2)
apple_response = json.dumps(getQuotes('AAPL'), indent=2)
tesla_response = json.dumps(getQuotes('TSLA'), indent=2)

# Convert the JSON responses to Python dictionaries.
alphabet_data = json.loads(alphabet_response.content)
apple_data = json.loads(apple_response.content)
tesla_data = json.loads(tesla_response.content)

print (alphabet_data)
print (apple_data)
print (tesla_data)

