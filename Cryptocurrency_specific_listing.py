import json
import requests

# array > dictionary to loop the requests
ticker_url = 'https://api.alternative.me/v2/ticker/?structure=array'

limit = 100
start = 1
sort = 'id'
convert = 'USD'

choice = input('DO you wish to enter specific parameters? (y/n): ')

if choice == 'y':
    limit = input('What is the custom limit?: ')
    start = input('What is the custom start number?: ')
    sort = input('What do you want to sort by?: ')
    convert = input('What is your local currency?: ')

ticker_url += '&limit=' + limit + '&sort=' + sort + '&start=' + start + '&convert=' + convert  