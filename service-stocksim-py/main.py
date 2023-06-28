import requests

from flask import Flask
from flask import request
from flask import Response

app = Flask(__name__)

@app.route('/')
def simulate_stock_price(methods=['GET', 'POST']):

    stock_symbol = request.args.get('stock')
    iterations_montecarlo  = request.args.get('iterations', default=1000000) #represents number of trading days
    
    if stock_symbol is None or stock_symbol == "":
       return Response("URL parameter stock not provided", status=200)

    #call API to get stock information
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

    #call the service-montecarlo-py to calculate the mean of the montecarlo iterations

    url_montecarlo = "http://montecarlo-svc:8080"
    #url_montecarlo = "http://127.0.0.1:8081"
    parameters = {
        "value" : stock_price,
        "iterations" : 100
    }

    #assign values to parameters
    # value = stock_price
    # iterations = iterations_montecarlo
    # for information in ["value", "iterations"]:      
    #     querystring_montecarlo[information] = eval(information)  

    #get response
    response_montecarlo = requests.get(f"{url_montecarlo}", params=parameters)
    response_data_montecarlo = response_montecarlo.json()
    print(response_data_montecarlo)

    return response_data_montecarlo

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
            