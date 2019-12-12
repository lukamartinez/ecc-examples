import matplotlib.pyplot as plt


def multiply_by(factor, curve):
    plt.xlim(0, curve.field.n)
    plt.ylim(0, curve.field.n)
    generated_point = factor * curve.g
    plt.scatter(generated_point.x, generated_point.y)
    plt.grid()
    plt.show()


def multiply_by_all_factors(max_factor, curve):
    plt.xlim(0, curve.field.n)
    plt.ylim(0, curve.field.n)
    for k in range(0, max_factor):
        p = k * curve.g
        print(f"{k} * G = ({p.x}, {p.y})")
        plt.scatter(p.x, p.y)
    plt.grid()
    plt.show()
