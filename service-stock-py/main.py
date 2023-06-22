import json

from flask import Flask
from flask import request
from flask import Response

import yfinance as yf

app = Flask(__name__)

@app.route('/')
def simulate_stock_price(methods=['GET', 'POST']):

    stock_symbol = request.args.get('stock')
    
    if stock_symbol is None or stock_symbol == "":
       return Response("URL parameter stock not provided", status=200)

    stock = yf.Ticker(stock_symbol)
    stockprice = stock.info['currentPrice']
    print (stockprice)
    
    return str(stockprice)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

