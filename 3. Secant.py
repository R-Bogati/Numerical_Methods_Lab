import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys 

eqn=input("Enter the equation in x using python syntax: ")
def F(x,eqn):
    return eval(eqn)
def f(x):
    return F(x,eqn)

print("Enter two initial guesses:")
a=float(input("Enter value of a: "))
b=float(input("Enter value of b:  "))

if f(a)==f(b):
    print("The value becomes infinte.Try other values")
else:
    e=float(input("Enter tolerable error: "))
    N=int(input("Enter maximum number of iterations: "))
    itr=1
    table=[]
    points=[]
    while itr<=N:
        c=(a*f(b)-b*f(a))/(f(b)-f(a))
        error=abs(c-b)
        table.append([itr,a,b,c,f(a),f(b),f(c),error])
        points.append(c)
        if error<e:
            table=pd.DataFrame(table,columns=('itr','a','b','c','f(a)','f(b)','f(c)','error'))
            print(table.to_string(index=False))
            print(f"The root is {c} in {itr} iterations")
            break
        a,b=b,c
        itr += 1
    
    if itr>N:
        print("Not enough iterations")
points=np.array(points)
x=np.linspace(-5,5,1000)
plt.plot(x,f(x),color='r', label=eqn)
plt.axhline(0,0,color='green')
plt.axvline(0,0,color='purple')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.title('Secant method')
plt.scatter(points,f(points))
for i,val in enumerate(points):
    plt.text(val,f(val),f'{i+1}')
plt.legend()
plt.show()

