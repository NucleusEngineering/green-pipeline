package main

import (
    "fmt"
    "math/rand"
)

func montecarlo_simulation(iterations, initial_stock_value float64) map[string]float64 {

    // Generate a random number generator.
    rng := rand.New(rand.NewSource(0))

    // Create a list to store the simulated stock prices.
    stock_prices := []float64{}

    // For each iteration, generate a random stock price.
    for _ in range(iterations):

        // Generate a random number between 0 and 1 and calculate with bandwidth.
        random_number := (rng.Float64() - 0.5) * 1.0

        // Calculate the new stock price.
        new_stock_price := initial_stock_value * (1 + random_number)

        // Add the new stock price to the list.
        stock_prices = append(stock_prices, new_stock_price)

    // Calc  mean & std of list of simulated stock prices.
    results := map[string]float64{
        "value_mean": np.mean(stock_prices),
        "value_std": np.std(stock_prices)
    }

    // Return the results
    return results
}