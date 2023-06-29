package main

import (
    "math/rand"
    "fmt"
)

func montecarloSimulation(iterations int, initialStockValue float64) map[string]float64 {

    stockPrices := []float64{}

    for i := 0; i < iterations; i++ {
        randomNumber := rand.Float64() - 0.5
        newStockPrice := initialStockValue * (1 + randomNumber)
        stockPrices = append(stockPrices, newStockPrice)
    }

    mean := float64(0)
    std := float64(0)
    for _, stockPrice := range stockPrices {
        mean += stockPrice
    }
    mean /= float64(len(stockPrices))

    for _, stockPrice := range stockPrices {
        std += (stockPrice - mean) * (stockPrice - mean)
    }
    std = math.Sqrt(std / float64(len(stockPrices)))

    result := map[string]float64{
        "value_mean": mean,
        "value_std": std,
    }

    return result
}

func main() {
    fmt.Println("Starting Monte Carlo simulation...")
    result := montecarloSimulation(1000, 100.0)
    fmt.Println("Simulation complete.")
    fmt.Println("Mean:", result["value_mean"])
    fmt.Println("Standard deviation:", result["value_std"])
}