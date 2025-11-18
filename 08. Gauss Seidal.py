import numpy as np
import pandas as pd

n=int(input("Enter number of variables: "))
A = []
print('Enter the coefficients:')
for i in range(n):
    A.append(list(map(float,input().split())))
A= np.array(A)
print('The augmented matrix is:')
print(A)

print('Enter Initial guess: ')
x=[]
for i in range(n):
    x.append(float(input()))
x = np.array(x)

print('Initial guess: ')
print(x)
e=float(input("Enter tolerable error: "))
N=int(input("Enter maximum number of iterations: "))
itr=1
T=[]
while itr<=N:
    xOld = np.copy(x)
    for i in range(n):
        s=0
        for j in range(n):
            if j!=i:
                s+=A[i,j]*x[j]
        if A[i,i]==0:
            print("divide by zero error")
        else:
            x[i]=(A[i,-1]-s)/A[i,i]
    err=np.abs(x-xOld)

    T.append([itr]+[x[i] for i in range(n)])
    if np.all(err<e):
        break
    itr+=1
if itr>N:
    print(f'Solution not found in {itr} iterations')
else:
    T=pd.DataFrame(T,columns=['iteration']+[f'x{i+1}' for i in range(n)])
    print(T.to_string(index=False))
    print('the solution is:')
    x= np.round(x, decimals=4)
    for i in range(n):
        print(f'x{i+1} = {x[i]}')




