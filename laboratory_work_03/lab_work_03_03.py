from math import *

def arctan(x, eps):
    step = 1000000
    n = 0
    val = pi/2
    while step >= eps:
        step = (-1**(n+1))/((2*n+1) * x**(2*n+1))
        val += step
        n += 1
    print(f"I   {x: 5.2f}   I   {val: 5.2f}  I  {n}  I")
print("+--------+--------+-----+")
print("I  X    I   Y    I   N I")


x_st = float(input("Введите точку начада из интервала x > 1"))
x_end = float(input("Введите точку конца из интервала x > 1"))
step = float(input("Введите шаг"))
eps = float(input("Введите значение ε погрешности"))

while x_st <= x_end:
    arctan(x_st, eps)
    x_st += step