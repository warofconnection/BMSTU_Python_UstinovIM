from math import (pi, sin, cos, tan, log)
x, y = input('Введите данные x, y: ').split()
x, y= int(x), int(y)
z1 = cos**4(x) + sin**2(y) + 1/4*sin**2(2*x) - 1
z2 = sin(y+x)*sin(y-x)
print(z1, z2)