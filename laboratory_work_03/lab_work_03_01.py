from math import *

print("Введите Xbeg, Xend и dx")
xb=float(input("Введите Xbeg: "))
xe=float(input("Введите Xend: "))
dx=float(input("Введите dx: "))

y=0

print("I    X   I    Y   I")
print("+--------+--------+")
while xb <= xe:

    if -10 <= xb <= -6:
        y = sqrt(4 - (xb + 8)**2) - 2
    elif -6 < xb <= 2:
        y = xb + 2
    elif 2 < xb < 6:
        y = 0
    elif 6 < xb <= 8:
        y = (xb-6)**2

    print("I{0: 7.2f} I{1: 7.2f} I".format(xb, y))
    xb += dx
print("+--------+--------+")

