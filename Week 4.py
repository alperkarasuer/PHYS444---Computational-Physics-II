# Coefficient matrices and number of unknowns
A = [[1, -1, 2, 1], [3, 2, 1, 4], [5, -8, 6, 3], [4, 2, 5, 3]]
b = [1, 1, 1, -1]
n = len(b)
x = [0.0] * n

# Initialization of index and scale vectors
indexVec = [0] * n
scaleVec = [0.0] * n

# Create index vector (starting from zero)
# and find the element with greatest abs() in each row
# to create scale vector
for i in range(n):
    indexVec[i] = i
    scaleMax = 0
    for j in range(n):
        if abs(A[i][j]) > scaleMax:
            scaleMax = abs(A[i][j])
    scaleVec[i] = scaleMax


# Forward elimination
for i in range(n - 1):
    ratioMax = 0.0
    # Find maximum of the ratios
    for j in range(i, n):
        ratio = abs(A[indexVec[j]][i]) / scaleVec[indexVec[j]]
        if ratio > ratioMax:
            ratioMax = ratio
            ratioIndex = j
    temp = indexVec[i]
    indexVec[i] = indexVec[ratioIndex]
    indexVec[ratioIndex] = temp

    # Update matrix
    for j in range(i + 1, n):
        mult = A[indexVec[j]][i] / A[indexVec[i]][i]
        for k in range(i, n):
            A[indexVec[j]][k] = A[indexVec[j]][k] - mult * A[indexVec[i]][k]
        b[indexVec[j]] = b[indexVec[j]] - mult * b[indexVec[i]]

# Backward substitution
x[n - 1] = b[indexVec[n - 1]] / A[indexVec[n - 1]][n - 1]
for j in range(n - 2, -1, -1):
    sumTotal = 0.0
    for k in range(j + 1, n):
        sumTotal = sumTotal + A[indexVec[j]][k] * x[k]
    x[j] = (b[indexVec[j]] - sumTotal) / A[indexVec[j]][j]


# Print the solution vector
for i in range(n):
    print("x{}".format(i+1) + " = {:.4f}".format((x[i])))
