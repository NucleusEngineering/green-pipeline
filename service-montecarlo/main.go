package main

import (
	"fmt"
	"math"
	"math/rand"
	"net/http"
	"os"
	"strconv"
)

func main() {
	// Create a new http server
	http.HandleFunc("/", montecarloSimulation)
	port := os.Getenv("PORT")

	fmt.Println("Starting server on port", port)
	err := http.ListenAndServe(fmt.Sprintf("0.0.0.0:%s", port), nil)
	if err != nil {
		panic(err)
	}

}

// This function simulates the stock price
func montecarloSimulation(w http.ResponseWriter, r *http.Request) {

	// Get the stock value, bandwidth and number of iterations from the request
	value := r.URL.Query().Get("value")
	bandwidth := r.URL.Query().Get("bandwidth")
	iterations := r.URL.Query().Get("iterations")

	// If the value is not provided, return an error
	if value == "" {
		http.Error(w, "Value not provided", http.StatusBadRequest)
		return
	}

	// Set default values if not provided
	if bandwidth == "" {
		bandwidth = "1.0"
	}
	if iterations == "" {
		iterations = "1000"
	}

	// casting to the right types
	iterationsInt, _ := strconv.Atoi(iterations)
	valueFloat, _ := strconv.ParseFloat(value, 64)
	bandwidthFloat, _ := strconv.ParseFloat(bandwidth, 64)

	results := montecarloSimulationCalc(iterationsInt, valueFloat, bandwidthFloat)

	// Write the response to the client
	fmt.Fprint(w, results)
}

func montecarloSimulationCalc(iterations int, initialStockValue float64, bandwidth float64) string {
	// Generate a random number generator.
	// Use a fixed seed for consistent results
	rng := rand.New(rand.NewSource(99))

	// Create a list to store the simulated stock prices.
	var stockPrices []float64

	// Simulate the stock price for the given number of iterations.
	for i := 0; i < iterations; i++ {
		// Generate a random number between -1 and 1.
		randomNum := rng.Float64()*2 - 1

		// Calculate the daily change in the stock price.
		dailyChange := initialStockValue * bandwidth * randomNum

		// Calculate the new stock price.
		newStockPrice := initialStockValue + dailyChange

		// Add the new stock price to the list.
		stockPrices = append(stockPrices, newStockPrice)

		// Update the initial stock value for the next iteration.
		initialStockValue = newStockPrice
	}

	// Calculate the mean of the simulated stock prices.
	var sum float64
	for _, price := range stockPrices {
		sum += price
	}
	mean := sum / float64(len(stockPrices))
	// Calculate the standard deviation of the simulated stock prices.
	var variance float64
	for _, price := range stockPrices {
		variance += math.Pow(price-mean, 2)
	}
	variance = variance / float64(len(stockPrices))
	stdDev := math.Sqrt(variance)

	// Return both the mean and standard deviation as a JSON object
	result := fmt.Sprintf(`{"value_mean": %f, "value_std": %f}`, mean, stdDev)
	return result

}
