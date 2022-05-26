import math

# Find the derivative by recursion
def D(n, m, x, h, f):
    phi = lambda s, delta: (f(s + delta) - f(s - delta)) / (2 * delta)
    if m != 0:
        result = D(n, m - 1, x, h, f) + (1 / (math.pow(4, m) - 1)) * (D(n, m - 1, x, h, f) - D(n - 1, m - 1, x, h, f))
    else:
        result = phi(x, h / (2 ** n))
    return result


def main():
    # Functions to calculate the derivative of
    f1 = lambda x: math.pow(x, math.cos(x))
    f2 = lambda x: math.pow(math.cos(100 * (x ** 2)), 5) / (x ** 3)

    print("D(5,5) estimate of derivative (in-class exercise): {:.4f}".format(D(5, 5, 0.6, 0.1, f1)))
    print("D(5,5) estimate of derivative (example): {:.4f}".format(D(5, 5, 1.3, 1 / 128, f2)))


main()
