import numpy as np
import random

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
 
  def montecarlo_simulation_calc(iterations, initial_stock_value):
 
    # Generate a random number generator.
    rng = random

    # Create a list to store the simulated stock prices.
    stock_prices = np.array(stock_prices)  # Convert to NumPy array
    
    mean = np.mean(stock_prices)
    std_dev = np.std(stock_prices)
    results = {
      "value_mean": mean,
      "value_std": std_dev
    }

    # Return the results
    return results

   
  
  return montecarlo_simulation_calc(iterations, value_float)  
  
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

  