import numpy as np
import matplotlib.pyplot as plt

a= float(input('Enter the lower limit: '))
b= float(input('Enter the upper limit: '))
func=input('Enter the integrand function in python syntax: ')

def F(x,func):
    return eval(func)
def y(x):
    return F(x,func)

n=int(input('Enter the number of partitions: '))
h=(b-a)/n
x=np.linspace(a,b,n+1)
s=0
I=0
for i in range(1,n):
    s+=y(x[i])
I=(h/2)*(y(x[0])+2*s+y(x[n]))
print('The approximate integral value is: ',I.round(6))

plt.plot(x,[y(x) for x in x],color='r')
x_val=np.linspace(a-10,b+10,1000)
plt.plot(x_val,[y(x) for x in x_val],color='b')
y_points=[y(x) for x in x]
for i in range(n):
    xs=[x[i],x[i+1],x[i+1],x[i]]
    ys=[0,0,y_points[i+1],y_points[i]]
    plt.fill(xs,ys,color='pink',edgecolor='black')
plt.axhline(0,0,color='green')
plt.axvline(0,0,color='purple')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.title('Trapezoidal Rule')
plt.show()