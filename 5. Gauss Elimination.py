import numpy as np

n=int(input("Enter number of variables: "))
matA = []
print('Enter the coefficients:')
for i in range(n):
    matA.append(list(map(float,input().split())))
matA = np.matrix(matA)
print('The augmented matrix is:')
print(matA)

for i in range(n):
    pivotRow = np.argmax(np.abs(matA[i:,i]))+i
    matA[[i,pivotRow]]=matA[[pivotRow,i]]      
    for j in range(i+1,n):
            matA[j]=matA[j]-(matA[j,i]/matA[i,i])*matA[i]

matA=np.matrix(matA)
print('The upper triangular matrix is:')
print(matA)
matA=np.array(matA)
x = np.zeros(n)
for i in range(n-1 , -1 , -1):
     x[i] = (matA[i, -1] - np.sum(matA[i, i+1:n] * x[i+1:n])) / matA[i, i]


print('The required solution are: ')
for i in range(n):
    print(x[i])
