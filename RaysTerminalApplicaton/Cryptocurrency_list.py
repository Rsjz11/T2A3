import json
import requests

listing_url = 'https://api.alternative.me/v2/listings/'

request = requests.get(listing_url)
results = request.json()

#print(json.dumps(results, sort_keys=True, indent=4))

data = results['data']

for currency in data: 
    rank = currency['id']  
    name = currency['name']
    symbol = currency['symbol']
    print(str(rank) + ': ' + name + ' (' + symbol + ')')

# This file when executed, lists the entire listing of cryptocurrencies up to 3799 