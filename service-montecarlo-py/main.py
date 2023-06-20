import numpy as np
import pandas as pd

from flask import Flask
from flask import request
from flask import Response

app = Flask(__name__)

@app.route('/')
def montecarlo_simulation(methods=['GET', 'POST']):
  
  value       = request.args.get('value')
  bandwidth   = request.args.get('bandwidth', default=1)
  iterations  = request.args.get('iteration', default=100)
  choice      = request.args.get('choice', default=5)

def monte_carlo_simulation(value, bandwidth, iterations, choice):

  updates = np.random.normal(0, 0.02, (choice, 1))
  value = np.zeros_like(updates)
  value[0] = value

  for i in range(1, iterations):
    value[i] = value[i - 1] * (1 + updates[i])

  return value


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

