import numpy as np
import matplotlib.pyplot as plt

# Given Constants
v0 = 5
g = 10

# Generate time and distance arrays
t = np.arange(0, 100, 1)
y = v0*t + 0.5*g*(t**2)

# Fit a polynomial to the data
poly = np.polyfit(t, y, 2)

# Plot data and polynomial
fig, ax = plt.subplots()
ax.plot(t, y, label = 'Data')
ax.plot(np.polyval(poly, t), 'o', markersize = 3, label = 'Polynomial Fit')

# Plot legends, labels, titles etc
ax.set(xlabel = 'Time (s)', ylabel = 'Distance (m)', title = 'Distance vs Time Plot')
ax.grid()
ax.legend()

plt.show()