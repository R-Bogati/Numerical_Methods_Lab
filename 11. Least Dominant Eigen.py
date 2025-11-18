#To find the least eigen value and the corresponding eigen vector of matrix using inverse power method.

import numpy as np
import sys
import pandas as pd

n = int(input('Enter the order of matrix: '))
A = []

for i in range(n):
    A.append(list(map(float,input(f'Enter row {i+1} :').split())))

A = np.array(A)
print('The matrix is A: \n',np.matrix(A))

def inv(A):
    try:
        return np.linalg.inv(A)
    except:
        print('Matrix is singular')
        sys.exit()

B = np.array(inv(A))
print('The inverse matrix is :\n',np.matrix(B))



x = np.array(list(map(float,input('Enter the initial vector:').split())))


print('The initial vector is: \n',np.matrix(x))

e = float(input('Enter tolerable error: '))
N = int(input('Enter the max number of iterations: '))
itr = 1
old_eigen = 0
t = []

while itr<=N:
    y = np.dot(B,x)
    max_eigen = abs(max(y,key=abs))


    x = y/max_eigen
    
    t.append([itr,max_eigen]+[x[i] for i in range(n)])
    error = abs(max_eigen-old_eigen)

    if (error<e):
        break
    
    old_eigen = max_eigen
    itr+=1

if (itr>N):
    print(f'Method doesnot converge in {itr} iterations.')
else:
    t = pd.DataFrame(t,columns=['iteration','Eigen Value']+[f'x{i+1}' for i in range(n)])
    print(t.to_string(index=False))
    print(f'The least eigen value is {1/max_eigen} in {itr} iterations')
    print('Corresponding eigen vector is: \n',x)

    