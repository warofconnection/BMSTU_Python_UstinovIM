from math import *
x, y = input('Введите данные x, y: ').split()
x, y= float(x), float(y)
z1 = cos(x)**4 + sin(y)**2 + 1/4*sin(2*x) - 1
z2 = sin(y+x)*sin(y-x)
print(z1, z2)