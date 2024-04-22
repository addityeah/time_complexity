import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit 
import subprocess
import time

class Fitting: 
    def calculate_execution_time(program_path):
        start_time = time.time()
        subprocess.run(["g++", program_path, "-o", "program"])
        subprocess.run(["./program"])
        end_time = time.time()
        execution_time = end_time - start_time
        return execution_time
    
    def check_output(program_path, ideal_soln):
        subprocess.run(["g++", program_path, "-o", "program"])
        subprocess.run(["g++", ideal_soln, "-o", "ideal_soln"])
        output = subprocess.run(["./program"], capture_output=True, text=True).stdout.strip()
        expected_output = subprocess.run(["./ideal_soln"], capture_output=True, text=True).stdout.strip()
        return output == expected_output
    
    def curve(x, a, b, c, d, e):
        return a*x**2 + b*np.log2(x)*x + c*x + d*np.log2(x) + e
    
def main():
    # subprocess.run(["python3 testcase_generator.py > testcases.txt"], shell=True)
    testcase_size = np.array([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101])
    time_taken = np.array([])

    # Fit the curve to the data using curve_fit
    fitp, fite = curve_fit(Fitting.curve(testcase_size), testcase_size, time_taken)
    
    curve = Fitting.curve(testcase_size, *fitp)

    plt.plot(testcase_size, curve, label='fit')
    plt.legend()
    plt.show()

    print(fite)

    return 0