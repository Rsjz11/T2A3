import json
import requests

listing_url = 'https://api.alternative.me/v2/listings/'

request = requests.get(listing_url)
results = request.json()

print(json.dumps(results, sort_keys=True, indent=4))