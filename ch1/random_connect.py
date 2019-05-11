"""
Exercise 1.1.31: `Random connections.`
Write a program that takes as command-line arguments an integer N
and a double value p (between 0 and 1), plots N equally spaced dots of size .05
on the circumference of a circle, and then, with probability p for each pair of points,
draws a gray line connecting them.
"""

import matplotlib.pyplot as plt
import numpy as np


show_flag = True

def set_no_show():
    show_flag = False

def draw(N, P):
    """
    Draw
    """

    # Plot the circle
    circle_theta = np.arange(0, 2 * np.pi, 2 * np.pi / 1000)
    circle_x = np.cos(circle_theta)
    circle_y = np.sin(circle_theta)

    plt.plot(circle_x, circle_y, color='r')

    # Plot the dots
    dot_theta = np.arange(0, 2 * np.pi, 2 * np.pi / N)
    dot_x = np.cos(dot_theta)
    dot_y = np.sin(dot_theta)
    plt.scatter(dot_x, dot_y, edgecolor="none", s=40)

    # Plot the line
    for i in range(N):
        for j in range(i + 1, N):
            if np.random.random() < P:
                line_x = [dot_x[i], dot_x[j]]
                line_y = [dot_y[i], dot_y[j]]
                plt.plot(line_x, line_y)
    # plt.tick_params(axis='both', which='major', labelsize=14)
    plt.axis('equal')
    plt.axis('off')
    if show_flag:
        print(show_flag)
        plt.show()


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        num, prob = 10, 0.3
    else:
        num, prob = int(sys.argv[1]), float(sys.argv[2])

    draw(num, prob)
