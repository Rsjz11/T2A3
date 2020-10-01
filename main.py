import json
import requests
# Figure out how to use URL
global_url = 'https://api.alternative.me/v2/global/'

request = requests.get(global_url)
results = request.json()

#print(json.dumps(results, sort_keys=True, indent=4))

active_currencies = results['data']['active_cryptocurrencies']
active_markets = results['data']['active_markets']
bitcoin_percentage = results['data']['bitcoin_percentage_of_market_cap']
last_updated = results['data']['last_updated']
global_cap = results['data']['quotes']['USD']['total_market_cap']
global_volume = results['data']['quotes']['USD']['total_volume_24h']

active_currencies_string = '{;,}'.format(active_currencies)
active_markets_string = '{;,}'.format(active_markets)
global_cap_string = '{;,}'.format(global_cap)
global_volume_string = '{;,}'.format(global_volume)

print()
print('There are currently ' + str(active_currencies) + ' active cryptocurrencies and ' + str(active_markets) + ' active markets.')
print('The global cap of all cryptocurrency is ' + str(global_cap) + ' and the 24h global volume is ' + str(global_volume) + '.')
print('Bitcoin\'s total percentage of the total global cap is ' + str(bitcoin_percentage) + '%.')
print()
print('This information was last updated on ' + str(last_updated) + '.')