import matplotlib.pyplot as plt
import numpy as np
import math


def draw_function(func, x_min, x_max):
    x = np.linspace(x_min, x_max, 1000)
    y = [func(i) for i in x]

    # Plot the graph
    plt.figure(figsize=(10,6))
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График функции')
    plt.grid(True)
    plt.show()