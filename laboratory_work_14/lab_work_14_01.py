import turtle
from math import sqrt

class FunctionPlotter:
    """Класс для построения графика кусочно-заданной функции"""

    def __init__(self, xb, xe, dx, scale=40):
        """
        Инициализация построителя графиков

        Args:
            xb: начальное значение X
            xe: конечное значение X
            dx: шаг
            scale: масштаб отображения
        """
        self.xb = xb
        self.xe = xe
        self.dx = dx
        self.scale = scale

        # Настройка turtle
        self.screen = None
        self.turtle = None

        self._setup_turtle()

    def _setup_turtle(self):
        """Настройка окна и черепашки"""
        self.screen = turtle.Screen()
        self.screen.setup(1000, 700)
        self.screen.title("График функции")
        self.screen.bgcolor("white")

        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.pensize(2)

    def calculate_y(self, x):
        """
        Вычисление значения функции в точке x

        Args:
            x: координата x

        Returns:
            значение y или None, если x вне области определения
        """
        if -10 <= x <= -6:
            return sqrt(4 - (x + 8) ** 2) - 2
        elif -6 < x <= 2:
            return x + 2
        elif 2 < x < 6:
            return 0
        elif 6 < x <= 8:
            return (x - 6) ** 2
        return None

    def draw_axes(self):
        """Рисование осей координат с делениями и подписями"""
        t = self.turtle
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

        # Подписи осей
        t.goto(460, -20)
        t.write("X", font=("Arial", 12, "normal"))
        t.goto(20, 360)
        t.write("Y", font=("Arial", 12, "normal"))

        # Деления на оси X
        for x in range(-10, 11):
            if x != 0:
                t.goto(x * self.scale, -5)
                t.pendown()
                t.goto(x * self.scale, 5)
                t.penup()
                if x % 2 == 0:
                    t.goto(x * self.scale, -20)
                    t.write(str(x), align="center", font=("Arial", 8, "normal"))

        # Деления на оси Y
        for y in range(-8, 9):
            if y != 0:
                t.goto(-5, y * self.scale)
                t.pendown()
                t.goto(5, y * self.scale)
                t.penup()
                if y % 2 == 0:
                    t.goto(-20, y * self.scale - 5)
                    t.write(str(y), align="right", font=("Arial", 8, "normal"))

        # Подпись нуля
        t.goto(-10, -15)
        t.write("0", font=("Arial", 8, "normal"))

    def draw_graph(self):
        """Рисование графика функции"""
        t = self.turtle
        t.penup()
        t.color("red")
        t.pensize(2)

        x = self.xb
        first_point = True

        while x <= self.xe:
            y = self.calculate_y(x)

            if y is not None:
                screen_x = x * self.scale
                screen_y = y * self.scale

                if first_point:
                    t.goto(screen_x, screen_y)
                    t.pendown()
                    first_point = False
                else:
                    t.goto(screen_x, screen_y)

            x += self.dx

        t.penup()

    def add_title(self):
        """Добавление заголовка графика"""
        self.turtle.penup()
        self.turtle.goto(0, 360)
        self.turtle.color("blue")
        self.turtle.write(
            f"График функции (dx={self.dx})",
            align="center",
            font=("Arial", 14, "bold")
        )

    def plot(self):
        """Основной метод для построения полного графика"""
        self.draw_axes()
        self.draw_graph()
        self.add_title()
        self.turtle.hideturtle()
        turtle.done()


def main():
    """Основная функция для получения данных от пользователя и построения графика"""
    print("Введите Xbeg, Xend и dx")

    xb = float(input("Введите Xbeg: "))
    xe = float(input("Введите Xend: "))
    dx = float(input("Введите dx: "))

    # Создаем экземпляр класса и строим график
    plotter = FunctionPlotter(xb, xe, dx)
    plotter.plot()


# Запуск программы
if __name__ == "__main__":
    main()