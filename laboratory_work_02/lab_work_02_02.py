from math import *

R = float(input("Введите значение для радиуса R: "))
x = float(input("Введите значение для переменной X: "))
y = float(input("Введите значение для переменной Y: "))

if  0 <= x <= R and x**2 + y**2 <= R**2 and -R <= y <= R:
    print("Точка внутри")
elif -y <= x <= 0 <= y <= R:
    print("Точка внутри")
elif y <= x <= 0 and -R <= y <= 0:
    print("Точка внутри")
else:
    print("Точка снаружи")