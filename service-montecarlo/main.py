import numpy as np

from flask import Flask
from flask import request
from flask import Response
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def montecarlo_simulation(methods=['GET', 'POST']):

  value       = request.args.get('value') #represents current stock price
  bandwidth   = request.args.get('bandwidth', default=1.0)
  iterations  = request.args.get('iterations', default=1000) #represents number of trading days 

  # casting to the right types
  iterations  = int(iterations)
  value_float = float(value)
  bandwidth   = float(bandwidth)
  results =  {}
 
  def montecarlo_simulation_calc(iterations, initial_stock_value):
 
    # Generate a random number generator.
    rng = np.random.default_rng()

    # Create a list to store the simulated stock prices.
    stock_prices = []

    # For each iteration, generate a random stock price.
    for _ in range(iterations):

      # Generate a random number between 0 and 1 and calculate with bandwidth.
      random_number = (rng.random() - 0.5) * bandwidth

      # Calculate the new stock price.
      new_stock_price = initial_stock_value * (1 + random_number)

      # Add the new stock price to the list.
      stock_prices.append(new_stock_price)
   
  
    # Calc  mean & std of list of simulated stock prices.
    results = {
      "value_mean": np.mean(stock_prices),
      "value_std": np.std(stock_prices)
    }  

    # Return the results
    return results
  
  return montecarlo_simulation_calc(iterations, value_float)  
  
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

  