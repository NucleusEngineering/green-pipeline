package main

import (
    "fmt"
    "net/http"
    "strings"
)

func main() {
    // Create a new http server
    http.HandleFunc("/", simulateStockPrice)
    err := http.ListenAndServe("0.0.0.0:8080", nil)
    if err != nil {
        panic(err)
    }
} 

// This function simulates the stock price
func simulateStockPrice(w http.ResponseWriter, r *http.Request) {

    // Get the stock symbol and number of iterations from the request
    stockSymbol := r.URL.Query().Get("stock")
    simIterations := r.URL.Query().Get("iterations")

    // If the stock symbol is not provided, return an error
    if stockSymbol == "" {
        http.Error(w, "Stock symbol not provided", http.StatusBadRequest)
        return
    }

    // Call the API to get stock information
    url := "https://yfapi.net/v6/finance/quote"
    querystring := make(map[string]string)
    querystring["symbols"] = stockSymbol

    headers := make(map[string]string)
    headers["x-api-key"] = "xKqFyxmTgdauCo4S1LRdD5adrSlyFK9J9if4VFfZ"

    response, err := http.Get(url, headers, querystring)
    if err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)
        return
    }

    // Get the stock price
    responseData := response.Body
    defer responseData.Close()
    stockPrice := strings.TrimSpace(string(responseData))

    // Call the service-montecarlo-py to calculate the mean of the montecarlo iterations
    urlMontecarlo := "http://montecarlo-svc:8080"

    parameters := make(map[string]string)
    parameters["value"] = stockPrice
    parameters["iterations"] = simIterations

    responseMontecarlo, err := http.Get(urlMontecarlo, parameters)
    if err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)
        return
    }

    // Get the response from the service-montecarlo-py
    responseMontecarloData := responseMontecarlo.Body
    defer responseMontecarloData.Close()
    mean := strings.TrimSpace(string(responseMontecarloData))

    // Write the response to the client
    fmt.Fprint(w, mean)
}