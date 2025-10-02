from math import *
from random import *

R=float(input("Введите значение для R: "))

print("I   X   I   Y   I Попадание I")
for n in range (10):
    x= uniform(-R,R)
    y= uniform(-R,R)
    if 0 <= x <= R and x ** 2 + y ** 2 <= R ** 2 and -R <= y <= R:
        print(f"I {x: 5.2f} I {y:5.2f} I Попал I")
    elif -y <= x <= 0 <= y <= R:
        print(f"I {x: 5.2f} I {y:5.2f} I Попал I")
    elif y <= x <= 0 and -R <= y <= 0:
        print(f"I {x: 5.2f} I {y:5.2f} I Попал I")
    else:
        print(f"I {x: 5.2f} I {y:5.2f} I Промах I")
print("I-------I-------I-----------I")