import numpy as np

n = int(input("Enter number of variables: "))
matA = []
print('Enter the coefficients:')
for i in range(n):
    matA.append(list(map(float, input().split())))

matA = np.matrix(matA)
print('The augmented matrix is:')
print(matA)

for i in range(n):
    pivotRow = np.argmax(np.abs(matA[i:, i])) + i
    matA[[i, pivotRow]] = matA[[pivotRow, i]]  # Swap rows
    matA[i] = matA[i] / matA[i, i]             # Make pivot = 1
    for j in range(n):
        if j != i:
            matA[j] = matA[j] - matA[j, i] * matA[i]
matA=np.array(matA)
print('The normal matrix is:')
print(np.round(matA, 6))  # Clean matrix display

x = matA[:, -1]
print('The required solution are: ')
for i in range(n):
    print(round(x[i], 6))
