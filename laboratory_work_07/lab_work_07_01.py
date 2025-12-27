from math import *
import turtle

# Получение данных от пользователя
print("Введите Xbeg, Xend и dx")
xb = float(input("Введите Xbeg: "))
xe = float(input("Введите Xend: "))
dx = float(input("Введите dx: "))

# Настройка turtle
screen = turtle.Screen()
screen.setup(1000, 700)
screen.title("График функции")
screen.bgcolor("white")

# Создаем черепашку
t = turtle.Turtle()
t.speed(0)
t.pensize(2)

# Масштаб для отображения
scale = 40


# Функция для вычисления Y
def calculate_y(x):
    if -10 <= x <= -6:
        return sqrt(4 - (x + 8) ** 2) - 2
    elif -6 < x <= 2:
        return x + 2
    elif 2 < x < 6:
        return 0
    elif 6 < x <= 8:
        return (x - 6) ** 2
    return None


# Рисуем оси координат
def draw_axes():
    t.penup()
    t.color("black")
    t.pensize(1)

    # Ось X
    t.goto(-450, 0)
    t.pendown()
    t.goto(450, 0)
    t.penup()

    # Ось Y
    t.goto(0, -350)
    t.pendown()
    t.goto(0, 350)
    t.penup()

    # Стрелки
    t.goto(450, 0)
    t.pendown()
    t.goto(440, 10)
    t.goto(450, 0)
    t.goto(440, -10)
    t.penup()

    t.goto(0, 350)
    t.pendown()
    t.goto(-10, 340)
    t.goto(0, 350)
    t.goto(10, 340)
    t.penup()

    # Подписи
    t.goto(460, -20)
    t.write("X", font=("Arial", 12, "normal"))
    t.goto(20, 360)
    t.write("Y", font=("Arial", 12, "normal"))

    # Деления на оси X
    for x in range(-10, 11):
        if x != 0:
            t.goto(x * scale, -5)
            t.pendown()
            t.goto(x * scale, 5)
            t.penup()
            if x % 2 == 0:
                t.goto(x * scale, -20)
                t.write(str(x), align="center", font=("Arial", 8, "normal"))

    # Деления на оси Y
    for y in range(-8, 9):
        if y != 0:
            t.goto(-5, y * scale)
            t.pendown()
            t.goto(5, y * scale)
            t.penup()
            if y % 2 == 0:
                t.goto(-20, y * scale - 5)
                t.write(str(y), align="right", font=("Arial", 8, "normal"))

    # Ноль
    t.goto(-10, -15)
    t.write("0", font=("Arial", 8, "normal"))


# Рисуем график
def draw_graph():
    t.penup()
    t.color("red")
    t.pensize(2)

    x = xb
    first_point = True

    while x <= xe:
        y = calculate_y(x)

        if y is not None:
            # Преобразуем координаты
            screen_x = x * scale
            screen_y = y * scale

            if first_point:
                t.goto(screen_x, screen_y)
                t.pendown()
                first_point = False
            else:
                t.goto(screen_x, screen_y)

        x += dx

    t.penup()



# Рисуем оси
draw_axes()

# Рисуем график
draw_graph()

# Добавляем заголовок
t.penup()
t.goto(0, 360)
t.color("blue")
t.write(f"График функции (dx={dx})", align="center", font=("Arial", 14, "bold"))

# Скрываем черепашку
t.hideturtle()


turtle.done()