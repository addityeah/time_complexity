import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit 

def curve(x, a, b, c, d, e):
    return a*x**2 + b*np.log2(x)*x + c*x + d*np.log2(x) + e
    
def main():
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    y = np.array([0, 0.8, 0.9, 0.1, -0.8, -1.0, -0.5, 0.4, 0.9, 1.0, 0.5, -0.4, -0.9, -1.0, -0.5, 0.4, 0.9, 1.0, 0.5, -0.4, -0.9])

    # Fit the curve to the data using curve_fit
    fitp, fite = curve_fit(curve, x, y)
    
    y5 = curve(x, *fitp)

    plt.plot(x, y5, label='fit')
    plt.legend()
    plt.show()

    print(fite)

    return 0