import numpy as np
from scipy.linalg import lu, lu_factor, lu_solve

n= int(input('Enter the number of variables: '))

A=[]
B=[]

for i in range(n):
    row=[]
    for j in range(n):
        row.append(float(input(f'Enter the elements of a{i+1}{j+1}: ')))
    A.append(row)
A=np.matrix(A)
print(f'The coeff matrix is A:\n {A}')

for i in range(n):
    row=[]
    for j in range(1):
        row.append(float(input(f'Enter the elements of b{i+1}{j+1}: ')))
    B.append(row)
B=np.matrix(B)
print(f'The output matrix is: \n {B}')

P,L,U = lu(A)
lum=lu_factor(A)
print(f'The lower triangular matrix L: \n {L}')
print(f'The upperr triangular matrix U: \n {U}')
print(f'The permutation matrix P: \n {P}')
X= lu_solve(lum,B)

print('The solution is: ')
X = np.array(X).flatten()
X= np.round(X, decimals=2)
for i in range(n):  
    print(f'x{i+1} = {X[i]}')