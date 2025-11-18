import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

eqn=input("Enter the equation in x using python syntax: ")
def F(x,eqn):
    return eval(eqn)
def f(x):
    return F(x,eqn)

print("Enter the two initial guess: \n")
a,b = float(input("Enter the value of a: ")), float(input("Enter the value of b: "))


if f(a) * f(b) > 0:
    print(f"No root lies in interval {a} and {b}")
else:
    e = float(input("Enter the value of tolerable error: "))
    N= int(input("Enter the number of iterations: "))
    itr = 1
    itr_table = []

    while itr <= N:
        c = (a + b) / 2
        
        itr_table.append([itr, a, b, c, f(a),f(b),f(c)])
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c

        er = abs((b - a) / b)
        # itr_table.append(er)

        if(er<e):
            itr_table = pd.DataFrame(itr_table, columns=['Itr', 'a', 'b', 'c', 'f(a)','f(b)','f(c)'])
            print(itr_table.to_string(index=False))
            print(f"Approximate root is: {(a+b)/2} in {itr} iteration")
            break
        itr += 1
    
    if itr > N:
        print(f"The solution doesn't reach in {N} iterations")
    else:
        print("End")

x = np.linspace(-5, 5, 1000)
plt.plot(x, f(x), label='f(x)', color='red')
plt.axhline(0,0,color = 'blue')
plt.axvline(0,0,color = 'green')
plt.grid(True)
plt.title('Bisection Method Function Plot')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()
