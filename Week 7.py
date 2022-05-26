import math

def gaussQuad(func, transformer, dxMult):

    # Look up table for weights and arguments
    twoPoint = [[1, -1/math.sqrt(3)], [1, 1/math.sqrt(3)]]

    # Transform the function to the [-1, 1] interval with the given
    # transforming function and multiply it by the constant which relates
    # dx to dx_d
    transformed = lambda xd: func(transformer(xd))*dxMult

    # Apply the formula
    acc = twoPoint[0][0]*transformed(twoPoint[0][1]) + twoPoint[1][0]*transformed(twoPoint[1][1])

    return acc

# Function to integrate
def f(x):
    return math.exp(x)*math.cos(x)

# Integral Limits
loLim = 0.5
hiLim = 1.5

# Transforming Function for Gauss-Quadrature Method
transformingFunc =lambda xd: (1/2)*((hiLim + loLim) + (hiLim - loLim)*xd)

# Crude way to find the coefficient when taking the derivative as the function is linear
multiplier = transformingFunc(2) - transformingFunc(1)

def main():
    print("Result of the Integral: {:.3f} ".format(gaussQuad(f, transformingFunc, multiplier)))

main()