import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def curve_func(n, a, option):
    if (option == 1):
        return a * n
    
    elif (option == 2):
        return a * n ** 2
    
    elif (option == 3):
        return a * np.log(n)
    
    elif (option == 4):
        return a * n * np.log(n)
    

def main():
    option = input("Enter the type of curve you want to fit: \n 1. Linear \n 2. Quadratic \n 3. Logarithmic \n 4. nlogn \n")
    
    curve = curve_func(option)
    
    x = np.array([0, 1, 2, 3, 4, 5])
    y = np.array([0, 0.8, 0.9, 0.1, -0.8, -1.0])

    # Fit the curve to the data using curve_fit
    params, covariance = curve_fit(curve, x, y)

    # Extract the fitted parameters
    a_fit = params

    # Generate y values using the fitted parameters
    y_fit = curve_func(x, a_fit)