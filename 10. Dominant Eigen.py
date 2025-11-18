#To find the dominant eigen value and the corresponding eigen vector of matrix using power method.

import numpy as np
import pandas as pd

n = int(input('Enter the order of matrix: '))
A = []

for i in range(n):
    A.append(list(map(float,input(f'Enter row {i+1}:').split())))

A = np.array(A)
print('The matrix is A: \n',np.matrix(A))

x = np.array(list(map(float,input('Enter initial vector:').split())))

print('The initial vector is: \n',np.matrix(x))

e = float(input('Enter tolerable error: '))
max_iter = int(input('Enter max number of iterations: '))
itr = 1
old_eigen = 0
t = []

while itr<=max_iter:
    y = np.dot(A,x)
    max_eigen = abs(max(y,key=abs))

    # Normalize the vector x
    x = y/max_eigen
        
    t.append([itr,max_eigen] + [x[i] for i in range(n)])   
    error = abs(max_eigen-old_eigen)

    if (error<e):
        break
    
    old_eigen = max_eigen
    itr+=1

if (itr>max_iter):
    print(f'Method does not converge in {max_iter} iterations.')
else:
    t = pd.DataFrame(t,columns = ['iteration', 'Eigen Value'] + [f'x{i+1}' for i in range(n)])
    print(t.to_string(index=False))
    print(f'The dominant eigen value is {max_eigen} in {itr-1} iterations')
    print('Corresponding eigen vector is: \n',x)



