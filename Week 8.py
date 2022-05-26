import math
import numpy as np
import matplotlib.pyplot as plt

# Function to solve for
def dudx(x, u):
    return (x**2)*math.exp(-(u+1))

# 2nd Order Runge Kutta - Heun's Method with a Single Corrector
def twoRK(f, tspan, initCond, step):
    t = np.arange(tspan[0], tspan[1] + step, step)
    numel = len(t)

    y = np.zeros(numel)
    y[0] = initCond

    for i in range(0, numel - 1):
        k1 = f(t[i], y[i])
        k2 = f(t[i] + step, y[i] + k1*step)
        y[i+1] = y[i] + (0.5 * k1 + 0.5 * k2)*step


    return t, y


def main():
    # Initial Conditions
    u0 = 1
    tInit = 0
    tFinal = 3
    step = 0.01

    # Function call
    time, soln = twoRK(dudx, [tInit, tFinal], u0, step)


    # Plotting
    fig, ax = plt.subplots()
    ax.plot(time, soln)
    ax.set(xlabel = 'x', ylabel = 'u(x)', title = 'Solution of the ODE')
    ax.grid()
    plt.show()


main()