"""
Exercise 1.1.31
"""

import matplotlib.pyplot as plt
import numpy as np


def draw():
    """
    Draw the dots
    """

    # Plot the circle
    theta = np.arange(0, 2 * np.pi, 2 * np.pi / 1000)

    x = np.cos(theta)
    y = np.sin(theta)

    plt.plot(x, y, color='r')

    # Plot the dots
    plt.scatter(0.5, 0.5, edgecolor="none", s=40)


    # plt.tick_params(axis='both', which='major', labelsize=14)
    plt.axis(aspect='equal')
    plt.show()


if __name__ == "__main__":
    draw()
