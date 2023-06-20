import json
from flask import Flask

from flask import request
from flask import Response

from yahoo_finance import Share



app = Flask(__name__)

@app.route('/simulate_stock_price')
def simulate_stock_price(methods=['GET', 'POST']):

    stock_symbol = request.args.get('stock')
    
    if stock_symbol is None or stock_symbol == "":
        return Response("URL parameter stock not provided", status=200)

    share = Share(stock_symbol)
    stockprice = share.get_price()

    print (stockprice)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

