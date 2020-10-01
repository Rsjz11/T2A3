import json
import requests
from datetime import datetime

currency = 'JPY'

global_url = 'https://api.alternative.me/v2/global/?convert=' + currency

request = requests.get(global_url)
results = request.json()

#print(json.dumps(results, sort_keys=True, indent=4))

active_currencies = results['data']['active_cryptocurrencies']
active_markets = results['data']['active_markets']
bitcoin_percentage = results['data']['bitcoin_percentage_of_market_cap']
last_updated = results['data']['last_updated']
global_cap = results['data']['quotes'][currency]['total_market_cap']
global_volume = results['data']['quotes'][currency]['total_volume_24h']

active_currencies_string = '{:,}'.format(active_currencies)
active_markets_string = '{:,}'.format(active_markets)
global_cap_string = '{:,}'.format(global_cap)
global_volume_string = '{:,}'.format(global_volume)

# strftime is a python built in module that changes a certain value by adding all the conversion specifier values. The value is the timestamp that will be converted to a calender date & time. 
last_updated_string = datetime.fromtimestamp(last_updated).strftime('%d %B, %Y at %I:%M%p ')

print()
print('There are currently ' + active_currencies_string + ' active cryptocurrencies and ' + active_markets_string + ' active markets.')
print('The global cap of all cryptocurrency is ' + global_cap_string + ' and the 24h global volume is ' + global_volume_string + '.')
print('Bitcoin\'s total percentage of the total global cap is ' + str(bitcoin_percentage) + ' %.')
print()
print('This information was last updated on ' + last_updated_string + '.')