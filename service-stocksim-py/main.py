import json
import requests

from flask import Flask
from flask import request
from flask import Response

app = Flask(__name__)

@app.route('/')
def simulate_stock_price(methods=['GET', 'POST']):

    stock_symbol = request.args.get('stock')
    
    if stock_symbol is None or stock_symbol == "":
       return Response("URL parameter stock not provided", status=200)

    url = "https://yfapi.net/v6/finance/quote"
    querystring = {}
    symbols = stock_symbol
    for information in ["symbols"]:      
        querystring[information] = eval(information)  

    headers = {
    'x-api-key': "xKqFyxmTgdauCo4S1LRdD5adrSlyFK9J9if4VFfZ"
    }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    response_data =  response.json()
    stock_price = response_data['quoteResponse']['result'][0]['regularMarketPrice']

    print(stock_price)
    
    # montecarlo

    return str(stock_price)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
            