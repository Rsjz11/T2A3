def json_request():
    request = requests.get(ticker_url)
    results = request.json()

def accepted_currency():
    currency = input("Please enter one of listed currencies: USD, EUR, GBP, RUB, JPY, CAD, KRW, PLN")
    if currency ==  USD', 'EUR', 'GBP', 'RUB', 'JPY', 'CAD', 'KRW', 'PLN':
        continue

