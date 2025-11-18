#To solve initial value problem of 1st order using the Euler (modified) method.
#qn y + np.exp(x), y(0) = 0, h = 0.1, n = any number
#no need to do this

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

ode = input("Enter dy/dx in terms of x and y using python syntax: ")

def F(x, y, ode):
    return eval(ode)

def f(x, y):
    return F(x, y, ode)

x = float(input("Enter the initial value of x: "))
y = float(input("Enter the initial value of y: "))
h = float(input("Enter the step size h: "))
n = int(input("Enter the number of steps n: "))
t =[]
xval = []
yval = []

for i in range(n):
    y_predict = y + h * f(x, y)
    y_correct = y + (h/2) * (f(x, y) + f(x + h, y_predict))
    y = y_correct
    x += h

    t.append((x, y))
    xval.append(x)
    yval.append(y)

t = pd.DataFrame(t, columns=['x', 'y'])
print("The solution of the initial value problem using Euler method is:")
print(t)

#for graph plot
plt.plot(xval, yval, label='Euler Method', color = "blue", linewidth = 2)
plt.scatter(xval, yval, color='red', label='Points', s= 50, zorder = 5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Euler Method')
plt.legend()
plt.grid()
plt.show()