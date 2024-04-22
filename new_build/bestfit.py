import matplotlib.pyplot as plt
import numpy as np

def func (x, a, b, c, d, e):
    return a*x^2 + b*x*np.log2(x) + c*x + d*np.log2(x)+ e

# Sample data
x_values = [1, 11, 111, 1111, 11111, 111111, 1111111]
y_values = [114.3, 105.3, 108.44, 127.5, 237.1, 1577.1, 20043.5]

# Plotting the graph
plt.plot(x_values, y_values)

# Adding labels and title
plt.xlabel('Testcase size')
plt.ylabel('Time taken')
plt.title('Graph')

# Displaying the graph
plt.show()