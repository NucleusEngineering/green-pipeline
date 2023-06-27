import numpy as np
import pandas as pd

from flask import Flask
from flask import request
from flask import Response

app = Flask(__name__)

@app.route('/')
def montecarlo_simulation(methods=['GET', 'POST']):

  value       = request.args.get('value') #represents current stock price
  #bandwidth   = request.args.get('bandwidth', default=1)
  iterations  = request.args.get('iteration', default=100) #represents number of trading days 
  #choice      = request.args.get('choice', default=5)
  value_float = float(value)
  '''def monte_carlo_simulation(value, bandwidth, iterations, choice):

    updates = np.random.normal(0, 0.02, (choice, 1))
    value = np.zeros_like(updates)
    print (value)
    value[0] = value

    for i in range(1, iterations):
      value[i] = value[i - 1] * (1 + updates[i])

    return value'''
  
  def montecarlo_simulation_calc(iterations, initial_stock_value):

    # Generate a random number generator.
    rng = np.random.default_rng()

    # Create a list to store the simulated stock prices.
    stock_prices = []

    # For each iteration, generate a random stock price.
    for _ in range(iterations):
      # Generate a random number between 0 and 1.
      random_number = rng.random()

      # Calculate the new stock price.
      new_stock_price = initial_stock_value * (1 + random_number)

      # Add the new stock price to the list.
      stock_prices.append(new_stock_price)

    stock_price_calc = np.mean(stock_prices)
    # Return mean of list of simulated stock prices.
    return stock_price_calc

  results = montecarlo_simulation_calc(iterations, value_float)  

  return str(results)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

