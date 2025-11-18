# Integration using Simpson's 3/8 rule
import numpy as np
import matplotlib.pyplot as plt

a = float(input('Enter the lower limit: '))
b = float(input('Enter the upper limit: '))
n = int(input("Enter the no. of sub intervals: "))

if n % 3 != 0:
    print("No. of sub intervals must be a multiple of 3!")
    exit()
else:
    func = input("Enter the integrand function in Python syntax: ")
    def F(x, func):
        return eval(func)
    def y(x):
        return F(x, func)
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    s1 = 0
    s2 = 0
    I = 0
    for i in range(1, n):
        if i % 3 != 0:
            s1 += y(x[i])
        else:
            s2 += y(x[i])

    I = (3*h / 8) * (y(x[0]) + 3 * s1 + 2 * s2 + y(x[n]))
    print(f'The integral by Simpson 3/8 rule is {I:.6f}')

    y_points = [y(x) for x in x]
    plt.plot(x, y_points)
    plt.scatter(x, y_points, color='b', label='Partition points')
    x_val = np.linspace(a - 10, b + 10, 1000)
    plt.plot(x_val, [y(x) for x in x_val], label='Integrand Function')
    for i in range(0, n, 3):
        x_list = x[i:i + 4]
        y_list = y_points[i:i + 4]
        plt.fill_between(x_list, y_list, color='pink', alpha=0.2)
    plt.axhline(0,0,color='green')
    plt.axvline(0,0,color='purple')
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Simpson 3/8 Rule')
    plt.legend()
    plt.show()
