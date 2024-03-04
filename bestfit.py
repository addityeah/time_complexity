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
    x = np.array([0, 1, 2, 3, 4, 5])
    y = np.array([0, 0.8, 0.9, 0.1, -0.8, -1.0])

    # Fit the curve to the data using curve_fit
    fitp0, fite0 = curve_fit(curve0, x, y)
    fitp1, fite1 = curve_fit(curve1, x, y)
    fitp2, fite2 = curve_fit(curve2, x, y)
    fitp3, fite3 = curve_fit(curve3, x, y)
    fitp4, fite4 = curve_fit(curve4, x, y)
    
    print(fite0, fite1, fite2, fite3, fite4)