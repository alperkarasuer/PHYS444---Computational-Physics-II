import matplotlib.pyplot as plt
import numpy as np
import math

# Given equation in exercise I and its derivative
eqn = lambda x: math.exp(-x/2) - 2*x*(math.cos(x)) + 5
eqnDerv = lambda x: -(math.exp(-x/2))/2 + 2*x*math.sin(x) - 2*math.cos(x)

# Force exerted by ring of charge
def coulomb(x):
    e0 = 8.85*(10**(-12))
    q = 2*(10**(-5))
    Q = 2*(10**(-5))
    a = 0.9
    force = (1/(4*math.pi*e0))*(q*Q*x)/(((x**2) + (a**2))**(3/2))

    return force - 1

def secant(f, guess, terminationCrit):
    # Initial Guesses
    xr = np.array([guess[0], guess[1]])

    # Initial Error
    err = xr[1] - xr[0]

    # Iteration Counter
    i = 0

    # Iterate until the criteria is met
    while err > terminationCrit:
        i += 1
        newGuess = xr[i] - (f(xr[i])*(xr[i-1] - xr[i]))/(f(xr[i-1]) - f(xr[i]))
        err = abs(newGuess - xr[i])
        xr = np.append(xr, newGuess)


    print("Root of the given equation is: {:.4f} found with {} iterations".format(xr[i], i+1))

    # Return the final element of guess array
    return xr[i]

def newton(f, fPrime, guess, terminationCrit):
    # Initial Guess
    xr = np.array(guess)

    # Run once to create error array
    firstGuess = xr - f(xr)/fPrime(xr)
    xr = np.append(xr, firstGuess)

    # Initial Error
    err = abs(firstGuess - xr[0])

    # Iteration Counter
    i = 1 # Start from one as we ran it once already

    # Iterate until the criteria is met
    while err > terminationCrit:
        newGuess = xr[i] - f(xr[i])/fPrime(xr[i])
        err = abs(newGuess - xr[i])
        xr = np.append(xr, newGuess)
        i += 1

    print("Root of the given equation is: {:.4f} found with {} iterations".format(xr[i], i+1))

    # Return the final element of guess array
    return xr[i]


def main():
    # Solution of In Class Exercise - I
    print("Solution of In Class Exercise - I")
    secant(eqn, [5, 5.1], 0.001)
    newton(eqn, eqnDerv, 5, 0.001)
    print("\n\n")


    # Solution of In Class Exercise - II

    # I suspect there would be two roots for this equation
    # So I plotted the graph and made guesses visually
    # I estimate the first root to be in the interval [0.1 0.3]
    # and the second root to be in the interval [1.3 1.6]

    # Use secant method with two of my guesses
    print("Solution of In Class Exercise - II")
    x1 = secant(coulomb, [0.1, 0.3], 0.001)
    x2 = secant(coulomb, [1.3, 1.6], 0.001)

    # Plot the graph and show the two roots found by secant method
    x = np.arange(0, 15, 0.1)
    y = np.array(coulomb(x))

    # Plot both the function and roots to show whether they are correct
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.plot(x1, coulomb(x1), 'ro', label = "First Root")
    ax.plot(x2, coulomb(x2), 'ro', label = "Second Root")
    ax.legend()
    ax.set(xlabel = "x (m)", ylabel = "Force - 1 (N)", title = "Solution Plot")
    ax.grid()
    plt.show()

# Run the main function
main()