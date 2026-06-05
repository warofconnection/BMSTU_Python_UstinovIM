import turtle
import random
import math
import time

class ShapeAnalyzer:
    """Класс для аналитического вычисления площади фигуры"""

    def __init__(self, R):
        """
        Инициализация анализатора фигуры

        Args:
            R: радиус круга и параметр треугольников
        """
        self.R = R

    def calculate_areas(self):
        """Вычисление площадей составных частей фигуры"""
        # Площадь четверти круга
        area_quarter_circle = (math.pi * self.R ** 2) / 4

        # Площадь двух треугольников
        area_triangles = 2 * (self.R ** 2 / 2)

        # Общая площадь
        real_area = area_quarter_circle + area_triangles

        return {
            'quarter_circle': area_quarter_circle,
            'triangles': area_triangles,
            'total': real_area
        }

    def display_analytical_result(self):
        """Вывод аналитического результата"""
        areas = self.calculate_areas()

        print("\n" + "=" * 60)
        print("1. АНАЛИТИЧЕСКОЕ ВЫЧИСЛЕНИЕ ПЛОЩАДИ")
        print("=" * 60)
        print(f"Площадь 1/4 круга: {areas['quarter_circle']:.4f}")
        print(f"Площадь двух треугольников: {areas['triangles']:.4f}")
        print(f"ОБЩАЯ РЕАЛЬНАЯ ПЛОЩАДЬ: {areas['total']:.4f}")
        print("=" * 60)

        return areas['total']


class MonteCarloSimulator:
    """Класс для проведения симуляции методом Монте-Карло"""

    def __init__(self, R, N=10000):
        """
        Инициализация симулятора Монте-Карло

        Args:
            R: радиус фигуры
            N: количество испытаний
        """
        self.R = R
        self.N = N
        self.inside_count = 0
        self.points_inside = []
        self.points_outside = []
        self.area_square = (2 * R) ** 2

    def is_point_inside(self, x, y):
        """
        Проверка попадания точки в фигуру

        Args:
            x: координата x
            y: координата y

        Returns:
            True если точка внутри фигуры, иначе False
        """
        # Первое условие: точка в правой части (x>=0) внутри круга
        if 0 <= x <= self.R and x ** 2 + y ** 2 <= self.R ** 2 and -self.R <= y <= self.R:
            return True
        # Второе условие: точка во втором квадранте (x<=0, y>=0) в треугольнике -y ≤ x ≤ 0
        elif -y <= x <= 0 <= y <= self.R:
            return True
        # Третье условие: точка в третьем квадранте (x≤0, y≤0) в треугольнике y ≤ x ≤ 0
        elif y <= x <= 0 and -self.R <= y <= 0:
            return True
        return False

    def run_simulation(self):
        """Запуск симуляции Монте-Карло"""
        print(f"Выполняется {self.N} испытаний...")
        start_time = time.time()

        for i in range(self.N):
            # Генерируем случайную точку в квадрате [-R, R] x [-R, R]
            x = random.uniform(-self.R, self.R)
            y = random.uniform(-self.R, self.R)

            if self.is_point_inside(x, y):
                self.inside_count += 1
                self.points_inside.append((x, y))
            else:
                self.points_outside.append((x, y))

            # Прогресс
            if (i + 1) % 2000 == 0:
                print(f"  Выполнено: {i + 1} испытаний")

        end_time = time.time()
        self.simulation_time = end_time - start_time

        return self.get_results()

    def get_results(self):
        """Получение результатов симуляции"""
        monte_carlo_area = (self.inside_count / self.N) * self.area_square

        return {
            'total_tests': self.N,
            'inside_points': self.inside_count,
            'outside_points': self.N - self.inside_count,
            'square_area': self.area_square,
            'monte_carlo_area': monte_carlo_area,
            'simulation_time': self.simulation_time
        }

    def display_results(self, real_area):
        """Вывод результатов симуляции"""
        results = self.get_results()

        error_percent = abs((results['monte_carlo_area'] - real_area) / real_area) * 100

        print("\nРЕЗУЛЬТАТЫ МЕТОДА МОНТЕ-КАРЛО:")
        print("-" * 40)
        print(f"Всего испытаний: {results['total_tests']}")
        print(f"Точек внутри фигуры: {results['inside_points']}")
        print(f"Точек вне фигуры: {results['outside_points']}")
        print(f"Площадь квадрата: {results['square_area']:.4f}")
        print(f"Оценка площади (Монте-Карло): {results['monte_carlo_area']:.4f}")
        print(f"Реальная площадь: {real_area:.4f}")
        print(f"Погрешность: {error_percent:.2f}%")
        print(f"Время вычисления: {results['simulation_time']:.3f} сек")
        print("=" * 60)

        return results['monte_carlo_area']


class MonteCarloVisualizer:
    """Класс для визуализации результатов метода Монте-Карло"""

    def __init__(self, R, points_inside, points_outside):
        """
        Инициализация визуализатора

        Args:
            R: радиус фигуры
            points_inside: список точек внутри фигуры
            points_outside: список точек вне фигуры
        """
        self.R = R
        self.points_inside = points_inside
        self.points_outside = points_outside
        self.scale = 300 / R  # Масштаб для отображения

        # Настройка окна
        self.screen = None
        self._setup_screen()

    def _setup_screen(self):
        """Настройка окна turtle"""
        self.screen = turtle.Screen()
        self.screen.setup(800, 800)
        self.screen.bgcolor("white")
        self.screen.tracer(0)  # Отключаем анимацию для ускорения

    def draw_axes(self):
        """Рисование осей координат"""
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
        for i in range(-int(self.R), int(self.R) + 1):
            if i != 0:
                axes.goto(i * self.scale, -5)
                axes.pendown()
                axes.goto(i * self.scale, 5)
                axes.penup()
                if abs(i) == int(self.R) or i == 0:
                    axes.goto(i * self.scale, -20)
                    axes.write(str(i), align="center", font=("Arial", 8, "normal"))

        # Деления на оси Y
        for i in range(-int(self.R), int(self.R) + 1):
            if i != 0:
                axes.goto(-5, i * self.scale)
                axes.pendown()
                axes.goto(5, i * self.scale)
                axes.penup()
                if abs(i) == int(self.R) or i == 0:
                    axes.goto(-25, i * self.scale - 5)
                    axes.write(str(i), align="right", font=("Arial", 8, "normal"))

        axes.hideturtle()

    def draw_points(self):
        """Рисование точек методом Монте-Карло"""
        # Точки ВНУТРИ фигуры - синие
        inside_turtle = turtle.Turtle()
        inside_turtle.speed(0)
        inside_turtle.penup()
        inside_turtle.color("blue")
        inside_turtle.shape("circle")
        inside_turtle.shapesize(0.15)

        for x, y in self.points_inside:
            inside_turtle.goto(x * self.scale, y * self.scale)
            inside_turtle.stamp()

        # Точки СНАРУЖИ фигуры - красные
        outside_turtle = turtle.Turtle()
        outside_turtle.speed(0)
        outside_turtle.penup()
        outside_turtle.color("red")
        outside_turtle.shape("circle")
        outside_turtle.shapesize(0.15)

        for x, y in self.points_outside:
            outside_turtle.goto(x * self.scale, y * self.scale)
            outside_turtle.stamp()

        inside_turtle.hideturtle()
        outside_turtle.hideturtle()

    def draw_square_boundary(self):
        """Рисование границы квадрата"""
        square = turtle.Turtle()
        square.speed(0)
        square.pensize(1)
        square.color("lightgray")
        square.penup()

        # Верхняя граница
        square.goto(-self.R * self.scale, self.R * self.scale)
        square.pendown()
        square.goto(self.R * self.scale, self.R * self.scale)

        # Правая граница
        square.goto(self.R * self.scale, -self.R * self.scale)

        # Нижняя граница
        square.goto(-self.R * self.scale, -self.R * self.scale)

        # Левая граница
        square.goto(-self.R * self.scale, self.R * self.scale)

        square.penup()
        square.hideturtle()

    def add_titles(self):
        """Добавление заголовков и подписей"""
        # Заголовок
        title = turtle.Turtle()
        title.penup()
        title.goto(0, 370)
        title.color("navy")
        title.write("МЕТОД МОНТЕ-КАРЛО: Определение площади фигуры",
                    align="center", font=("Arial", 14, "bold"))
        title.hideturtle()

        # Формула фигуры
        formula = turtle.Turtle()
        formula.penup()
        formula.goto(0, -310)
        formula.color("darkgreen")
        formula.write("Фигура: часть круга (x≥0) + два треугольника (x≤0)",
                      align="center", font=("Arial", 10, "italic"))
        formula.hideturtle()

    def visualize(self):
        """Основной метод визуализации"""
        self.draw_axes()
        self.draw_square_boundary()
        self.draw_points()
        self.add_titles()

        self.screen.update()  # Обновляем экран
        self.screen.tracer(1)  # Включаем анимацию обратно
        turtle.done()


class MonteCarloApp:
    """Главный класс приложения, объединяющий все компоненты"""

    def __init__(self):
        """Инициализация приложения"""
        self.R = None
        self.analyzer = None
        self.simulator = None
        self.visualizer = None
        self.real_area = None

    def run(self):
        """Запуск приложения"""
        # Получаем радиус от пользователя
        self.R = float(input("Введите значение для радиуса R: "))

        # 1. Аналитическое вычисление
        self.analyzer = ShapeAnalyzer(self.R)
        self.real_area = self.analyzer.display_analytical_result()

        # 2. Симуляция Монте-Карло
        N = 10000  # Количество испытаний
        self.simulator = MonteCarloSimulator(self.R, N)
        self.simulator.run_simulation()
        self.simulator.display_results(self.real_area)

        # 3. Визуализация
        self.visualizer = MonteCarloVisualizer(
            self.R,
            self.simulator.points_inside,
            self.simulator.points_outside
        )
        self.visualizer.visualize()


# Запуск программы
if __name__ == "__main__":
    app = MonteCarloApp()
    app.run()