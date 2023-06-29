import requests

from flask import Flask
from flask import request
from flask import Response

app = Flask(__name__)

@app.route('/')
def simulate_stock_price(methods=['GET', 'POST']):

    stock_symbol = request.args.get('stock')
    sim_iterations  = request.args.get('iterations', default=1000) 
    
    if stock_symbol is None or stock_symbol == "":
       return Response("URL parameter stock must be provided", status=200)
 
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
 
    #call the service-montecarlo-py to calculate the mean of the montecarlo iterations
    url_montecarlo = "http://montecarlo-svc:8080"
 
    parameters = {
        "value" : stock_price,
        "iterations" : sim_iterations
    }
    
    #execute the call
    response_montecarlo = requests.get(f"{url_montecarlo}", params=parameters)
    response_data_montecarlo = response_montecarlo.json()
    print(response_data_montecarlo)

    return response_data_montecarlo

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
            