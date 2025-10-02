from math import *

x = float(input('Введите значение X=:'))
if -10 <= x < -6:
    y = sqrt(4 - (x + 8)**2) - 2
if -6 <= x < 2:
    y = x + 2
if 2 <= x < 6:
    y = 0
if 6 <= x < 8:
    y = (x-6)**2
print('x = {0:.2f} y = {1:.2f}'.format(x, y))