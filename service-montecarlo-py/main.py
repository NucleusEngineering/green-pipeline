import numpy as np
import pandas as pd

from flask import Flask
from flask import request
from flask import Response

app = Flask(__name__)

@app.route('/montecarlo')
def montecarlo_simulation(methods=['GET', 'POST']):
  
  value       = request.args.get('value')
  bandwidth   = request.args.get('bandwidth', default=1)
  iterations  = request.args.get('iteration', default=100)
  choice      = request.args.get('choice', default=5)

def monte_carlo_simulation(value, bandwidth, iterations, choice):

  daily_returns = np.random.normal(0, 0.02, (n_iterations, 1))
  stock_prices = np.zeros_like(daily_returns)
  stock_prices[0] = stock_price

  for i in range(1, n_iterations):
    stock_prices[i] = stock_prices[i - 1] * (1 + daily_returns[i])

  return stock_prices

if __name__ == "__main__":
  stock_price = 100
  n_iterations = 1000
  stock_prices = monte_carlo_simulation(stock_price, n_iterations)

  print(stock_prices)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

