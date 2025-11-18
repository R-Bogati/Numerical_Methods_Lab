# To fit the second degree curve y = a + bx + cx^2 using least square method to given data
import numpy as np
import matplotlib.pyplot as plt

X = np.array(list(map(float, input("Enter all x data :").split())))
Y = np.array(list(map(float, input("Enter all y data :").split())))
n = len(X)

A = [[n, np.sum(X), np.sum(X**2)],
     [np.sum(X), np.sum(X**2), np.sum(X**3)],
     [np.sum(X**2), np.sum(X**3), np.sum(X**4)]]

B = [[np.sum(Y)],[np.sum(X*Y)],[np.sum((X**2)*Y)]]

print("The coefficient matrix of normal equation is :\n", np.matrix(A))
print("Constant term of normal equations :\n", np.matrix(B))

inv_A = np.linalg.inv(A)
print("The inverse matrix is \n", np.matrix(inv_A))

coeff = np.dot(inv_A, B)
     
a = coeff[0].item()
b = coeff[1].item()
c = coeff[2].item()

print(f"The curve of best fit is: y = {a:.4f} + ({b:.4f})x + ({c:.4f})x²")

x = np.linspace(min(X)-5, max(X)+5, 1000)
plt.plot(x, a + b*x + c*x**2, color='r', label='Fitted curve')
plt.scatter(X, Y, color='b', label='Data points')
plt.axhline(0, color='gray')
plt.axvline(0, color='gray')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Curve fitting')
plt.legend()
plt.grid(True)
plt.show()

#1 2 3 4 5 6 7
#-5 -2 5 16 31 50 73