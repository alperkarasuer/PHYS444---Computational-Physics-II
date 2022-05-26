import numpy as np
import matplotlib.pyplot as plt


def dydx(x, y, z):
    return -2 * y + 4 * np.exp(-x)


def dzdx(x, y, z):
    return -(y * (z ** 2)) / 3


# Initiate the problem
xInit = 0
xFinal = 1
step = 0.2

y0 = 2
z0 = 4

# Create arrays for solution
x = np.arange(xInit, xFinal + step, step, dtype = float)
solnEuler = np.zeros((np.size(x), 2), dtype = float)
solnRK = np.zeros((np.size(x), 2), dtype = float)

solnEuler[0, :] = [y0, z0]
solnRK[0, :] = [y0, z0]

# Euler's Method
for i in range(0, np.size(x) - 1):
    # Euler's Method
    solnEuler[i + 1, 0] = solnEuler[i, 0] + step * dydx(x[i], solnEuler[i, 0], solnEuler[i, 1])
    solnEuler[i + 1, 1] = solnEuler[i, 1] + step * dzdx(x[i], solnEuler[i, 0], solnEuler[i, 1])

    # 4th Order Runge-Kutta Method
    k11 = dydx(x[i], solnRK[i, 0], solnRK[i, 1])
    k12 = dzdx(x[i], solnRK[i, 0], solnRK[i, 1])

    k21 = dydx(x[i] + step / 2, solnRK[i, 0] + k11 * step / 2, solnRK[i, 1] + k12 * step / 2)
    k22 = dzdx(x[i], solnRK[i, 0] + k11 * step / 2, solnRK[i, 1] + k12 * step / 2)

    k31 = dydx(x[i] + step / 2, solnRK[i, 0] + k21 * step / 2, solnRK[i, 1] + k22 * step / 2)
    k32 = dzdx(x[i], solnRK[i, 0] + k21 * step / 2, solnRK[i, 1] + k22 * step / 2)

    k41 = dydx(x[i] + step, solnRK[i, 0] + k31 * step, solnRK[i, 1] + k32 * step)
    k42 = dzdx(x[i], solnRK[i, 0] + k31 * step, solnRK[i, 1] + k32 * step)

    solnRK[i + 1, 0] = solnRK[i, 0] + (1 / 6) * (k11 + 2 * (k21 + k31) + k41) * step
    solnRK[i + 1, 1] = solnRK[i, 1] + (1 / 6) * (k12 + 2 * (k22 + k32) + k42) * step


# Print the solutions
print("###############")
print("Euler's Method")
print("###############")
print("x\t\t y\t\t z")
for i in range(0, np.size(x)):
    print("{:.2f}\t{:.2f}\t{:.2f}".format(x[i], solnEuler[i, 0], solnEuler[i, 1]))

print("\n")

print("#############################")
print("4th Order Runge-Kutta Method")
print("#############################")
print("x\t\t y\t\t z")
for i in range(0, np.size(x)):
    print("{:.2f}\t{:.2f}\t{:.2f}".format(x[i], solnRK[i, 0], solnRK[i, 1]))



# Plot the solutions
fig1, ax1 = plt.subplots()
ax1.plot(x, solnEuler[:, 0], label = 'Euler')
ax1.plot(x, solnRK[:, 0], label = '4RK')
ax1.set(xlabel = "x", ylabel = "y", title = "y vs x")
ax1.grid()
ax1.legend()

fig2, ax2 = plt.subplots()
ax2.plot(x, solnEuler[:, 1], label = 'Euler')
ax2.plot(x, solnRK[:, 1], label = '4RK')
ax2.set(xlabel = "x", ylabel = "z", title = "z vs x")
ax2.grid()
ax2.legend()

plt.show()

