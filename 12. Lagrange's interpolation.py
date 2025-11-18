import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

X=np.array(list(map(float,input('Enter all x-data: ').split())))
Y=np.array(list(map(float,input('Enter all y-data: ').split())))
n=len(X)
x=sp.symbols('x')
L_poly=0
for i in range(n):
    lbp=1
    for j in range(n):
        if j!=i:
            lbp*=(x-X[j])/(X[i]-X[j])
    L_poly += Y[i]*lbp
L_poly=sp.simplify(L_poly)
print('The Lagrange interpolation polnomial is:\n',L_poly)

xp=float(input('Enter the value to interpolate: '))
int_val=L_poly.subs(x,xp)
print(f'The interpolated value at x-{xp} is: {int_val.round(6)}')

poly1=sp.lambdify(x,L_poly,'numpy')
x_val=np.linspace(min(X)-5,max(X)+5,1000)
plt.plot(x_val,poly1(x_val),color='r',label='Lagrange polynomial')
plt.axhline(0,0,color='green')
plt.axvline(0,0,color='purple')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.scatter(X,Y,marker='o',color='blue',label='Data points')
plt.scatter(xp,poly1(xp),marker='x',color='brown',label='Interpolated point')
plt.title('Lagrange interpolation')
plt.legend()
plt.show()
