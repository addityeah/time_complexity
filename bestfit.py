import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit 
import EvaluateSubmissions as es

def curve(x, a, b, c, d, e):
    return a*x**2 + b*np.log2(x)*x + c*x + d*np.log2(x) + e
    
def main():
    testcase_size = np.array([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101])
    time_taken = np.array()

    # Fit the curve to the data using curve_fit
    fitp, fite = curve_fit(curve, testcase_size, time_taken)
    
    fitting_curve = curve(testcase_size, *fitp)

    plt.plot(testcase_size, fitting_curve, label='fit')
    plt.legend()
    plt.show()

    print(fite)

    return 0