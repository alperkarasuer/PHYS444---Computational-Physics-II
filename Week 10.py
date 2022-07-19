import numpy as np
import matplotlib.pyplot as plt

# Problem Constants
L = 20
h = 0.1
N = 200
s = 0.9
k = h*np.sqrt(s)
a = 5 # My selection for parameter alpha


# Initialization of Matrices
xValues = np.linspace(0, L, N) # N equally spaced values for x between 0 and L
tValues = np.linspace(0, k*N, N) # N equally spaced values for t between 0 and k*N
phiValues = np.zeros(len(xValues)) # Initialize phi as a vector of zeros
psiValues = np.zeros(len(xValues)) # Initialize psi as a vector of zeros
u = np.zeros((len(tValues), len(xValues))) # Initialize u as a matrix of zeros


# Function Definitions
def phi(x):
	return np.exp(-a*(x-L/2)**2)

def psi(x):
	return 0

def populate(u, psiVals, phiVals, xVals, tVals):
	for j in range(len(xVals)):
		phiVals[j] = phi(xVals[j])
		psiVals[j] = psi(xVals[j])

	return solver(u, psiVals, phiVals, xVals, tVals)


def solver(u, psiVals, phiVals, xVals, tVals):
	# u^0_j --> t = 0
	for j in range(len(xVals)):
		u[0][j] = phiVals[j] # Formula in page 30

	# u^1_j --> t = 1
	for j in range(1, len(xVals) - 1):
		u[1][j] = (0.5)*s*(phiVals[j+1] + phiVals[j-1]) + (1-s)*phiVals[j] + k*psiVals[j] # Formula in page 30

	# t > 1
	for n in range(1, len(tVals) - 1):
		for j in range(1, len(xVals) - 1):
			u[n+1][j] = s*(u[n][j+1] + u[n][j-1]) + 2*(1-s)*u[n][j] - u[n-1][j] # Formula in page 29

	return u

def exact(x, t):
	arr = []
	for i in range(len(x)//2):
		arr.append(0.5*(phi(x[i] + t[i]) + phi(x[i] - t[i])))
	for i in range(len(x)//2, len(x)):
		arr.append(0.5*(phi(x[-i] + t[-i]) + phi(x[-i] - t[-i])))
	return arr
	

# Solutions
soln = populate(u, psiValues, phiValues, xValues, tValues)
numSoln = soln[52] # Solution at t = 52 was closest to the exact solution
exactSoln = exact(xValues, tValues)



# Plotting
fig, ax = plt.subplots()
ax.plot(xValues, phiValues, color='black', label='Initial Condition')
ax.plot(xValues, numSoln, color='blue', label='Numerical Solution')
ax.plot(xValues, exactSoln, color='red', label='Exact Solution')
ax.legend()
ax.grid()
ax.set(xlabel = 'x', ylabel = 'u', title = 'Comparison of Exact and Numerical Solutions')
plt.show()
