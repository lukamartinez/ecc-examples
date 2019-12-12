import matplotlib.pyplot as plt
import numpy as np


def visualize_elliptic_curve(a, b):
    y, x = np.ogrid[-5:5:100j, -5:5:100j]
    plt.contour(x.ravel(), y.ravel(), pow(y, 2) - pow(x, 3) - x * a - b, [0])
    plt.grid()
    plt.show()


def visualize_simplified_elliptic_curve(a, b, p):
    for x in range(0, p):
        for y in range(0, p):
            if (pow(y, 2) - pow(x, 3) - x * a - b) % p == 0:
                print(f"(x, y) = ({x}, {y})")
                plt.scatter(x, y)
    plt.grid()
    plt.show()
