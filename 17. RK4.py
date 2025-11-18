# To solve initial value problem of 1st order by R-K-4 method
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ode = input("Enter dy/dx in terms of x and y using python syntax: ")

def F(x, y, ode):
    return eval(ode)

def f(x, y):
    return F(x, y, ode)

x = float(input("Enter the initial value of x: "))
y = float(input("Enter the initial value of y: "))
h = float(input("Enter step size: "))
n = int(input("Enter number of steps: "))

t = []
x_val = []
y_val = []

for i in range(n):
    k1 = h * f(x, y)
    k2 = h * f(x + (h / 2), y + (k1 / 2))
    k3 = h * f(x + (h / 2), y + (k2 / 2))
    k4 = h * f(x + h, y + k3)
    
    y = y + (1/6) * (k1 + 2*k2 + 2*k3 + k4)
    x = x + h

    t.append([x, y])
    x_val.append(x)
    y_val.append(y)

result = pd.DataFrame(t, columns=['x', 'y'])
print(result.to_string(index=False))

plt.plot(x_val, y_val, color='r', label='RK-4 Approximation')
plt.scatter(x_val, y_val, color='b', label='Data points')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('RK-4 method')
plt.legend()
plt.grid(True)
plt.show()
