import numpy as np
import pandas as pd

def monte_carlo_simulation(stock_price, n_iterations):
  """
  Performs a Monte Carlo simulation on a stock price with n iterations.

  Args:
    stock_price: The current stock price.
    n_iterations: The number of iterations to perform.

  Returns:
    A list of stock prices, one for each iteration.
  """

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