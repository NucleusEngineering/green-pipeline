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
  results = {}
 
  def montecarlo_simulation_calc(iterations, initial_stock_value, bandwidth):
    # Generate random numbers for all iterations at once
    random_numbers = (np.random.rand(iterations) - 0.5) * bandwidth
    # Calculate stock prices using vectorized operations
    stock_prices = initial_stock_value * (1 + random_numbers)
    # Calculate mean and standard deviation
    results = {
        "value_mean": np.mean(stock_prices),
        "value_std": np.std(stock_prices)
    }
    return results

   
  
  return montecarlo_simulation_calc(iterations, value_float)  
  
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

  