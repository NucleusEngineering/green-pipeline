package main

import (
    "fmt"
    "math/rand"
)

func main() {
    // Set the number of iterations.
    n := 1000

    // Initialize the stock price.
    price := 100

    // Create a slice to store the simulated stock prices.
    simulatedPrices := make([]float64, n)

    // Perform the Monte Carlo simulation.
    for i := 0; i < n; i++ {
        // Generate a random number between 0 and 1.
        randomNumber := rand.Float64()

        // Calculate the simulated stock price.
        simulatedPrices[i] = price * (1 + randomNumber)
    }

    // Print the simulated stock prices.
    for i := 0; i < n; i++ {
        fmt.Println(simulatedPrices[i])
    }
}