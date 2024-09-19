import unittest
import main  # Assuming your service code is in main.py

class TestMonteCarlo(unittest.TestCase):

    def test_mean_std_calculation(self):
        # Test case 1: 1000 iterations, bandwidth 0.5
        iterations = 1000
        bandwidth = 0.5
        initial_stock_value = 100  # You might want to get this from an actual stock API

        # Call your service function 
        mean, std_dev = main.montecarlo_simulation(initial_stock_value, bandwidth, iterations) 

        # Assert that the results are within an acceptable range
        self.assertAlmostEqual(mean, 100, delta=0.5)  # Adjust delta as needed
        self.assertAlmostEqual(std_dev, 12.5, delta=1) # Adjust delta as needed

if __name__ == '__main__':
    unittest.main()
