import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

eqn=input("Enter the equation in x using python syntax: ")
def F(x,eqn):
    return eval(eqn)
def f(x):
    return F(x,eqn)
def g(f,x,h=1e-10):
    return(f(x+h)-f(x))/h

a=float(input("Enter initial guess: "))

if g(f,a)==0:
    print("Try another value")

else:
    e=float(input("Enter tolerable error: "))
    N=int(input("Enter maximum iterations: "))
    itr=1
    table=[]
    points=[]
    while itr<=N:
        b=a-f(a)/g(f,a)
        error=abs(b-a)
        table.append([itr,a,b,f(a),g(f,a),error])
        points.append(b)
        if error<e:
            table=pd.DataFrame(table,columns=('itr','a','b','f(a)',"f'(a)",'error'))
            print(table.to_string(index=False))
            print(f"The root is {b} in {itr} iterations")
            break
        a=b
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
plt.title('Newton_Raphson method')
plt.scatter(points,f(points))
for i,val in enumerate(points):
    plt.text(val,f(val),f'{i+1}')
plt.legend()
plt.show()
