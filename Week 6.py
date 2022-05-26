import numpy as np


# Probability distribution function
def pdf(x):
    return (1 / (2.8 * np.sqrt(2 * np.pi))) * np.exp(-((x - 69) ** 2) / 5.6)


# Unit conversion
def cmToInch(x):
    return x / 2.54


# Simpson's Rule for Integration
def simpson(f, tspan, step):
    # Integration span
    t = np.arange(tspan[0], tspan[1] + step, step)

    # Number of triplets to use
    binCount = (np.size(t) - 1) // 2
    bins = np.zeros(shape = (binCount, 3))
    discreteAreas = np.zeros(shape = (binCount, 2))

    # Generate triplets
    for i in range(binCount):
        bins[i, :] = [t[2 * i], t[2 * i + 1], t[2 * i + 2]]

    # Apply formula to fill discreteAreas matrix
    for i in range(1, binCount + 1):
        discreteAreas[i - 1, 1] = (1 / 6) * (bins[i - 1, 2] - bins[i - 1, 0]) * (
                    f(bins[i - 1, 0]) + 4 * f(bins[i - 1, 1]) + f(bins[i - 1, 2]))
        discreteAreas[i - 1, 0] = bins[i - 1, 2]

    # Sum over discreteAreas to find accumulated area
    for i in range(2, np.size(discreteAreas[:, 1]) + 1):
        discreteAreas[i - 1, 1] = discreteAreas[i - 1, 1] + discreteAreas[i - 2, 1]

    # Total sum of areas
    acc = discreteAreas[-1, 1]

    return discreteAreas, acc


def main():
    limLo = 150  # cm
    limHi = 182  # cm
    dh = 0.1  # cm

    # Function call
    bins, acc = simpson(pdf, [cmToInch(limLo), cmToInch(limHi)], cmToInch(dh))

    # Print the results
    print("Probability of height being between {} cm and {} cm is {:.2f}%".format(limLo, limHi, acc * 100))
    print("Integral Step Size: {} cm".format(dh))


main()
