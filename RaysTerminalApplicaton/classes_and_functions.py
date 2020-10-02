def json_request():
    request = requests.get(ticker_url)
    results = request.json()

