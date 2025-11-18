# To evaluate integration from a to b f(x) using Simpson Rule
import numpy as np
import matplotlib.pyplot as plt

a = float(input('Enter the lower limit: '))
b = float(input('Enter the upper limit: '))
n = int(input('Enter the no. of partitions: '))

if n % 2 != 0:
    print('Number of partitions must be Even!')
    exit()
else:
    func = input('Enter the integrand function in terms of x: ')
    def F(x, func):
        return eval(func)
    def y(x):
        return F(x, func)

    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    s1 = 0
    s2 = 0
    I=0
    for i in range(1, n):
        if i % 2 != 0:
            s1 += y(x[i])
        else:
            s2 += y(x[i])

    I = (h / 3) * (y(x[0]) + 4 * s1 + 2 * s2 + y(x[n]))
    print(f'The integral by Simpson 1/3 rule is {I:.6f}')

    y_points = [y(x) for x in x]
    plt.plot(x, y_points)
    plt.scatter(x, y_points, color='b', label='Partition points')
    x_val = np.linspace(a - 10, b + 10, 1000)
    plt.plot(x_val, [y(x) for x in x_val],color='r', label='Integrand Function')
    for i in range(0, n, 2):
        x_list = x[i:i + 3]
        y_list = y_points[i:i + 3]
        plt.fill_between(x_list, y_list, color='pink', alpha=0.2)
    plt.axhline(0,0,color='green')
    plt.axvline(0,0,color='purple')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Simpson 1/3 Rule')
    plt.legend()
    plt.grid(True)
    plt.show()
