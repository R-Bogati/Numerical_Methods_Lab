# To solve the system of linear equation by Jacobian Method.


import numpy as np
import pandas as pd

n = int(input("Enter the number of variables : "))
A = []

print("Enter the elements for augmented matrix ")

# input for augmented matrix
for i in range(n):
    row = []
    for j in range(n+1):
        row.append(float(input(f"Element a{i+1}{j+1} : ")))
    A.append(row)
    
A = np.matrix(A)
print(f"\nThe augmented matrix is : ")
print(A)


# input for column
X = []
T = []


print("\nEnter the elements for X ")
for i in range(n):
    X.append(float(input(f"Enter initial guess {i+1} : ")))
    
X = np.array(X).reshape(n, 1)

e,N = float(input("Enter tolerable error : ")), int(input("Enter the no. of max iteration : "))
itr = 1


while itr <= N :
    X_old = np.copy (X)
    for i in range (n):
        s = 0
        for j in range (n):
            if j != i:
                s += A[i, j] * X_old[j]
        X[i] = (A[i, -1] - s) / A[i, i]

    err = np.abs(X - X_old)

    T.append([itr] + [X[i,0] for i in range (n)])  

    if np.all(err < e):
        break
    itr += 1

if itr > N :
    print (f"Solution doesn't converge in {N} iteration.")

else:

    T = pd.DataFrame(T, columns = ["iteration"] + [f"X{i+1}" for i in range (n) ]).to_string(index=False)
    print ("\nTable")
    print (f"\n{T}")
    print ("\nThe solution using Jacobian method is : ")
    for i in range (n):
        print (f"X{i+1} = {X[i, 0]}")

    print (f"in {i} iteration(s).")




