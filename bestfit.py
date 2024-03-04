import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit 

def curve0(a):
    return a

def curve1(x, a, b):
    return a * x + b

def curve2(x, a, b, c):
    return a * x**2 + b * x + c

def curve3(x, a, b):
    return a * np.log2(x) + b

def curve4(x, a, b, c):
    return a * np.log2(x) * x + b * x + c
    
def main():
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    y = np.array([0, 0.8, 0.9, 0.1, -0.8, -1.0, -0.5, 0.4, 0.9, 1.0, 0.5, -0.4, -0.9, -1.0, -0.5, 0.4, 0.9, 1.0, 0.5, -0.4, -0.9])

    # Fit the curve to the data using curve_fit
    fitp0, fite0 = curve_fit(curve0, x, y)
    fitp1, fite1 = curve_fit(curve1, x, y)
    fitp2, fite2 = curve_fit(curve2, x, y)
    fitp3, fite3 = curve_fit(curve3, x, y)
    fitp4, fite4 = curve_fit(curve4, x, y)
    
    y1 = curve0(x, *fitp0)
    y1 = curve0(x, *fitp0)
    y2 = curve1(x, *fitp1)
    y3 = curve2(x, *fitp2)
    y4 = curve3(x, *fitp3)
    y5 = curve4(x, *fitp4)

    plt.plot(x, y, 'o', label='data')
    plt.plot(x, y1, label='fit0')
    plt.plot(x, y2, label='fit1')
    plt.plot(x, y3, label='fit2')
    plt.plot(x, y4, label='fit3')
    plt.plot(x, y5, label='fit4')
    plt.legend()
    plt.show()

    print(fite0)
    print(fite1)
    print(fite2)
    print(fite3)
    print(fite4)

    return 0