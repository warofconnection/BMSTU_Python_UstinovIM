import turtle
import random
import math
import time

# Получаем радиус от пользователя
R = float(input("Введите значение для радиуса R: "))

# 1. АНАЛИТИЧЕСКОЕ ВЫЧИСЛЕНИЕ ПЛОЩАДИ
print("\n" + "=" * 60)
print("1. АНАЛИТИЧЕСКОЕ ВЫЧИСЛЕНИЕ ПЛОЩАДИ")
print("=" * 60)


# Площадь четверти круга
area_quarter_circle = (math.pi * R ** 2) / 4

area_triangles = 2 * (R ** 2 / 2)

# Общая площадь
real_area = area_quarter_circle + area_triangles

print(f"Площадь 1/4 круга: {area_quarter_circle:.4f}")
print(f"Площадь двух треугольников: {area_triangles:.4f}")
print(f"ОБЩАЯ РЕАЛЬНАЯ ПЛОЩАДЬ: {real_area:.4f}")
print("=" * 60)

# Количество испытаний
N = 10000

# Область, в которую вписана фигура: квадрат [-R, R] x [-R, R]
area_square = (2 * R) ** 2  # Площадь квадрата, содержащего фигуру


# Функция проверки попадания точки в фигуру (ТОЧНО по вашему коду)
def is_point_inside(x, y):
    # Первое условие: точка в правой части (x>=0) внутри круга
    if 0 <= x <= R and x ** 2 + y ** 2 <= R ** 2 and -R <= y <= R:
        return True
    # Второе условие: точка во втором квадранте (x<=0, y>=0) в треугольнике -y ≤ x ≤ 0
    elif -y <= x <= 0 <= y <= R:
        return True
    # Третье условие: точка в третьем квадранте (x≤0, y≤0) в треугольнике y ≤ x ≤ 0
    elif y <= x <= 0 and -R <= y <= 0:
        return True
    return False


# Выполняем испытания
inside_count = 0
points_inside = []
points_outside = []

print(f"Выполняется {N} испытаний...")
start_time = time.time()

for i in range(N):
    # Генерируем случайную точку в квадрате [-R, R] x [-R, R]
    x = random.uniform(-R, R)
    y = random.uniform(-R, R)

    if is_point_inside(x, y):
        inside_count += 1
        points_inside.append((x, y))
    else:
        points_outside.append((x, y))

    # Прогресс
    if (i + 1) % 2000 == 0:
        print(f"  Выполнено: {i + 1} испытаний")

# Оцениваем площадь по методу Монте-Карло
monte_carlo_area = (inside_count / N) * area_square

# Оценка точности
error_percent = abs((monte_carlo_area - real_area) / real_area) * 100

end_time = time.time()

print("\nРЕЗУЛЬТАТЫ МЕТОДА МОНТЕ-КАРЛО:")
print("-" * 40)
print(f"Всего испытаний: {N}")
print(f"Точек внутри фигуры: {inside_count}")
print(f"Точек вне фигуры: {N - inside_count}")
print(f"Площадь квадрата: {area_square:.4f}")
print(f"Оценка площади (Монте-Карло): {monte_carlo_area:.4f}")
print(f"Реальная площадь: {real_area:.4f}")
print(f"Погрешность: {error_percent:.2f}%")
print(f"Время вычисления: {end_time - start_time:.3f} сек")
print("=" * 60)


# Настройка окна
screen = turtle.Screen()
screen.setup(800, 800)
screen.title(f"Метод Монте-Карло (R={R}, N={N})")
screen.bgcolor("white")
screen.tracer(0)  # Отключаем анимацию для ускорения

# Масштаб для отображения
scale = 300 / R  # Чтобы фигура поместилась в окно 600x600


# Функция для отрисовки осей
def draw_axes():
    axes = turtle.Turtle()
    axes.speed(0)
    axes.pensize(1)
    axes.color("gray")
    axes.penup()

    # Ось X
    axes.goto(-350, 0)
    axes.pendown()
    axes.goto(350, 0)
    axes.penup()

    # Ось Y
    axes.goto(0, -350)
    axes.pendown()
    axes.goto(0, 350)
    axes.penup()

    # Стрелки
    axes.goto(340, 10)
    axes.pendown()
    axes.goto(350, 0)
    axes.goto(340, -10)
    axes.penup()

    axes.goto(10, 340)
    axes.pendown()
    axes.goto(0, 350)
    axes.goto(-10, 340)
    axes.penup()

    # Подписи осей
    axes.goto(360, -15)
    axes.write("X", font=("Arial", 12, "normal"))
    axes.goto(10, 360)
    axes.write("Y", font=("Arial", 12, "normal"))

    # Деления на оси X
    for i in range(-int(R), int(R) + 1):
        if i != 0:
            axes.goto(i * scale, -5)
            axes.pendown()
            axes.goto(i * scale, 5)
            axes.penup()
            if abs(i) == int(R) or i == 0:
                axes.goto(i * scale, -20)
                axes.write(str(i), align="center", font=("Arial", 8, "normal"))

    # Деления на оси Y
    for i in range(-int(R), int(R) + 1):
        if i != 0:
            axes.goto(-5, i * scale)
            axes.pendown()
            axes.goto(5, i * scale)
            axes.penup()
            if abs(i) == int(R) or i == 0:
                axes.goto(-25, i * scale - 5)
                axes.write(str(i), align="right", font=("Arial", 8, "normal"))

    axes.hideturtle()


# Рисуем точки Монте-Карло
def draw_points():
    # Точки ВНУТРИ фигуры - синие
    inside_turtle = turtle.Turtle()
    inside_turtle.speed(0)
    inside_turtle.penup()
    inside_turtle.color("blue")
    inside_turtle.shape("circle")
    inside_turtle.shapesize(0.15)  # Маленькие точки

    for i, (x, y) in enumerate(points_inside):
        inside_turtle.goto(x * scale, y * scale)
        inside_turtle.stamp()

    # Точки СНАРУЖИ фигуры - красные
    outside_turtle = turtle.Turtle()
    outside_turtle.speed(0)
    outside_turtle.penup()
    outside_turtle.color("red")
    outside_turtle.shape("circle")
    outside_turtle.shapesize(0.15)  # Маленькие точки


    for i, (x, y) in enumerate(points_outside):
        outside_turtle.goto(x * scale, y * scale)
        outside_turtle.stamp()

    inside_turtle.hideturtle()
    outside_turtle.hideturtle()



# Рисуем границу квадрата
def draw_square_boundary():
    square = turtle.Turtle()
    square.speed(0)
    square.pensize(1)
    square.color("lightgray")
    square.penup()

    # Верхняя граница
    square.goto(-R * scale, R * scale)
    square.pendown()
    square.goto(R * scale, R * scale)

    # Правая граница
    square.goto(R * scale, -R * scale)

    # Нижняя граница
    square.goto(-R * scale, -R * scale)

    # Левая граница
    square.goto(-R * scale, R * scale)

    square.penup()
    square.hideturtle()


# Рисуем все элементы
draw_axes()
draw_square_boundary()  # Квадрат, в котором генерируются точки
draw_points()


# Заголовок
title = turtle.Turtle()
title.penup()
title.goto(0, 370)
title.color("navy")
title.write("МЕТОД МОНТЕ-КАРЛО: Определение площади фигуры",
            align="center", font=("Arial", 14, "bold"))
title.hideturtle()

# Отображаем формулу фигуры
formula = turtle.Turtle()
formula.penup()
formula.goto(0, -310)
formula.color("darkgreen")
formula.write("Фигура: часть круга (x≥0) + два треугольника (x≤0)",
              align="center", font=("Arial", 10, "italic"))
formula.hideturtle()

screen.update()  # Обновляем экран
screen.tracer(1)  # Включаем анимацию обратно

turtle.done()