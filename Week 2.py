import numpy as np
import math
import matplotlib.pyplot as plt

# Arguments: Temperature as Kelvin and Oxygen Saturation to solve for.
def f(t, oxySat):
    rhs = -139.34411 + ((1.575701 * (10**5))/t) - ((6.642308 * (10**7))/(t**2)) + ((1.243800 * (10**10))/(t**3)) - ((8.621949 * (10**11))/(t**4))
    return rhs - np.log(oxySat)

# Bisection Method Function
def bisection(oxygenVal, errLim, xlInit, xuInit):

    # Find number of iterations with formula
    n = math.ceil(np.log((xuInit - xlInit) / errLim) / np.log(2) + 1)
    print("{} Iterations are required to an absolute error of {}".format(n, errLim))

    # Convert brackets to Kelvin
    xl = xlInit + 273.15
    xu = xuInit + 273.15

    # Start Iteration
    for i in range(0, n):
        xr = (xl + xu) / 2

        if f(xl, oxygenVal) * f(xr, oxygenVal) < 0:
            xu = xr
        elif f(xl, oxygenVal) * f(xr, oxygenVal) > 0:
            xl = xr
        elif f(xl, oxygenVal) * f(xr, oxygenVal) == 0:
            break

    # Convert Kelvin back to Celsius
    tempResult = xr - 273.15
    print("For Oxygen Saturation {}, temperature required is {:.2f} found with brackets {} and {}\n".format(oxygenVal, tempResult, xlInit, xuInit))

    return tempResult

# Call the functions with respective arguments
soln1 = bisection(8, 0.05, 0, 40)
soln2 = bisection(10, 0.05, 0, 40)
soln3 = bisection(12, 0.05, 0, 40)

# Plot the results to see the check the results visually
t = np.arange(0, 40, 0.1)
f1 = f(t + 273.15, 8)
f2 = f(t + 273.15, 10)
f3 = f(t + 273.15, 12)

fig, ax = plt.subplots()
ax.plot(t, f1, label="Oxygen Saturation 8")
ax.plot(t, f2, label="Oxygen Saturation 10")
ax.plot(t, f3, label="Oxygen Saturation 12")
ax.plot(soln1, 0, 'ro')
ax.plot(soln2, 0, 'ro')
ax.plot(soln3, 0, 'ro')
ax.set(xlabel = "Temperature (C)", ylabel = "f(T) - ln(O2)", title = "Solution Plot")
ax.grid()
ax.legend()