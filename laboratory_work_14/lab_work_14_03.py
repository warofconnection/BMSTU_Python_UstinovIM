import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import math


class TaylorSeries:
    """Класс для вычисления рядов Тейлора"""

    @staticmethod
    def calculate_term(x, n):
        """Вычисление n-го члена ряда Тейлора для функции y(x) = ∑ (-1)ⁿ·x²ⁿ/n!"""
        return ((-1) ** n) * (x ** (2 * n)) / math.factorial(n)

    @staticmethod
    def compute_y(x, epsilon):
        """
        Вычисление y(x) с помощью ряда Тейлора с заданной точностью

        Args:
            x: значение аргумента
            epsilon: точность вычислений

        Returns:
            значение функции y(x)
        """
        result = 0.0
        term = 1.0  # n=0: (-1)^0 * x^0 / 0! = 1
        n = 0

        while abs(term) > epsilon:
            result += term
            n += 1
            term = TaylorSeries.calculate_term(x, n)

        return result


class FunctionCalculator:
    """Класс для вычисления различных функций"""

    def __init__(self, epsilon):
        """
        Инициализация калькулятора функций

        Args:
            epsilon: точность вычислений для рядов Тейлора
        """
        self.epsilon = epsilon
        self.taylor_series = TaylorSeries()

    def y_function(self, x):
        """Обертка для вычисления y(x)"""
        return self.taylor_series.compute_y(x, self.epsilon)

    @staticmethod
    def z_function(x, b):
        """
        Вычисление z(x) = e^(-x^2) + b

        Args:
            x: значение аргумента
            b: параметр функции

        Returns:
            значение функции z(x)
        """
        return math.exp(-x ** 2) + b

    def generate_data(self, x_start, x_end, dx, b):
        """
        Генерация данных для построения графиков

        Args:
            x_start: начальное значение X
            x_end: конечное значение X
            dx: шаг
            b: параметр для функции z(x)

        Returns:
            кортеж (x_values, y_values, z_values)
        """
        x_values = np.arange(x_start, x_end + dx, dx)
        y_values = [self.y_function(x) for x in x_values]
        z_values = [self.z_function(x, b) for x in x_values]

        return x_values, y_values, z_values


class Plotter:
    """Класс для построения графиков"""

    def __init__(self, parent_frame):
        """
        Инициализация построителя графиков

        Args:
            parent_frame: родительский фрейм для размещения графика
        """
        self.parent_frame = parent_frame
        self.fig = None
        self.ax = None
        self.canvas = None

        self._setup_plot()

    def _setup_plot(self):
        """Настройка области для построения графиков"""
        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        self.ax.set_title("Графики функций y(x) и z(x)", fontsize=14, fontweight='bold')
        self.ax.set_xlabel("Ось X", fontsize=12)
        self.ax.set_ylabel("Ось Y", fontsize=12)
        self.ax.grid(True, alpha=0.3)
        self.ax.legend()

        # Создаем холст Tkinter для matplotlib
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.parent_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def update_plots(self, x_values, y_values, z_values, epsilon, b):
        """
        Обновление графиков новыми данными

        Args:
            x_values: значения X
            y_values: значения Y для первой функции
            z_values: значения Z для второй функции
            epsilon: точность вычислений
            b: параметр функции
        """
        # Очищаем предыдущий график
        self.ax.clear()

        # Строим новые графики
        self.ax.plot(x_values, y_values, 'b-', linewidth=2,
                     label=f'y(x) (ряд Тейлора, ε={epsilon})')
        self.ax.plot(x_values, z_values, 'r-', linewidth=2,
                     label=f'z(x) = e^(-x²) + {b}')

        # Настройки графика
        self.ax.set_title("Графики функций y(x) и z(x)", fontsize=14, fontweight='bold')
        self.ax.set_xlabel("Ось X", fontsize=12)
        self.ax.set_ylabel("Ось Y", fontsize=12)
        self.ax.grid(True, alpha=0.3)
        self.ax.legend(loc='best')

        # Автоматическое масштабирование
        self.ax.autoscale(enable=True, axis='both', tight=True)

        # Обновляем холст
        self.canvas.draw()


class InputValidator:
    """Класс для валидации входных данных"""

    @staticmethod
    def validate_range(x_start, x_end):
        """Проверка корректности диапазона X"""
        if x_start >= x_end:
            raise ValueError("X начальное должно быть меньше X конечного")
        return True

    @staticmethod
    def validate_positive(value, param_name):
        """Проверка, что значение положительное"""
        if value <= 0:
            raise ValueError(f"{param_name} должен быть положительным")
        return True

    @staticmethod
    def validate_all(x_start, x_end, dx, epsilon):
        """Комплексная проверка всех параметров"""
        InputValidator.validate_range(x_start, x_end)
        InputValidator.validate_positive(dx, "Шаг dx")
        InputValidator.validate_positive(epsilon, "Точность ε")
        return True


class InputFrame:
    """Класс для создания и управления панелью ввода"""

    def __init__(self, parent, callback_on_update):
        """
        Инициализация панели ввода

        Args:
            parent: родительский контейнер
            callback_on_update: функция обратного вызова при обновлении
        """
        self.parent = parent
        self.callback_on_update = callback_on_update

        # Параметры по умолчанию
        self.b = 0.0
        self.x_start = -3.0
        self.x_end = 3.0
        self.dx = 0.01
        self.epsilon = 1e-6

        # Создаем виджеты
        self._create_widgets()

    def _create_widgets(self):
        """Создание виджетов панели ввода"""
        control_frame = ttk.LabelFrame(self.parent, text="Параметры", padding="10")
        control_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), padx=5, pady=5)

        # Поле для параметра b
        ttk.Label(control_frame, text="Параметр b:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.b_entry = ttk.Entry(control_frame, width=15)
        self.b_entry.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        self.b_entry.insert(0, "0.0")

        # Поля для диапазона x
        ttk.Label(control_frame, text="X начальное:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.x_start_entry = ttk.Entry(control_frame, width=15)
        self.x_start_entry.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        self.x_start_entry.insert(0, "-3.0")

        ttk.Label(control_frame, text="X конечное:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.x_end_entry = ttk.Entry(control_frame, width=15)
        self.x_end_entry.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
        self.x_end_entry.insert(0, "3.0")

        # Поле для шага
        ttk.Label(control_frame, text="Шаг dx:").grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        self.dx_entry = ttk.Entry(control_frame, width=15)
        self.dx_entry.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)
        self.dx_entry.insert(0, "0.01")

        # Поле для точности
        ttk.Label(control_frame, text="Точность ε:").grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
        self.epsilon_entry = ttk.Entry(control_frame, width=15)
        self.epsilon_entry.grid(row=4, column=1, sticky=tk.W, padx=5, pady=5)
        self.epsilon_entry.insert(0, "1e-6")

        # Кнопки
        ttk.Button(control_frame, text="Построить графики",
                   command=self._on_update).grid(row=5, column=0, columnspan=2, pady=10)
        ttk.Button(control_frame, text="Выход",
                   command=self._on_exit).grid(row=6, column=0, columnspan=2, pady=5)

    def _on_update(self):
        """Обработчик нажатия кнопки обновления"""
        try:
            self._get_values_from_entries()
            self.callback_on_update()
        except ValueError as e:
            messagebox.showerror("Ошибка ввода", str(e))
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")

    def _on_exit(self):
        """Обработчик выхода из приложения"""
        self.parent.quit()

    def _get_values_from_entries(self):
        """Получение значений из полей ввода с валидацией"""
        self.b = float(self.b_entry.get())
        self.x_start = float(self.x_start_entry.get())
        self.x_end = float(self.x_end_entry.get())
        self.dx = float(self.dx_entry.get())
        self.epsilon = float(self.epsilon_entry.get())

        # Валидация
        InputValidator.validate_all(self.x_start, self.x_end, self.dx, self.epsilon)

    def get_parameters(self):
        """
        Получение всех параметров

        Returns:
            словарь с параметрами
        """
        return {
            'b': self.b,
            'x_start': self.x_start,
            'x_end': self.x_end,
            'dx': self.dx,
            'epsilon': self.epsilon
        }


class InfoPanel:
    """Класс для отображения информационной панели с описанием функций"""

    def __init__(self, parent):
        """
        Инициализация информационной панели

        Args:
            parent: родительский контейнер
        """
        self.parent = parent
        self._create_panel()

    def _create_panel(self):
        """Создание информационной панели"""
        info_frame = ttk.LabelFrame(self.parent, text="Функции", padding="10")
        info_frame.grid(row=0, column=3, rowspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)

        info_text = """y(x) = ∑ (-1)ⁿ·x²ⁿ/n!
    (ряд Тейлора)

z(x) = e^{-x²} + b

b - параметр, вводимый с клавиатуры"""

        ttk.Label(info_frame, text=info_text, justify=tk.LEFT).pack(padx=5, pady=5)


class Lab8App:
    """Главный класс приложения"""

    def __init__(self, root):
        """
        Инициализация приложения

        Args:
            root: корневой элемент Tkinter
        """
        self.root = root
        self.root.title("Лабораторная работа №8 - Графики функций")

        # Установка размеров окна
        self._setup_window_size()

        # Создание компонентов
        self.function_calculator = None
        self.plotter = None
        self.input_frame = None
        self.info_panel = None

        # Создание интерфейса
        self._create_interface()

        # Построение начальных графиков
        self.update_graphs()

    def _setup_window_size(self):
        """Настройка размера окна"""
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = int(screen_width * 0.8)
        window_height = int(screen_height * 0.8)
        self.root.geometry(f"{window_width}x{window_height}")

    def _create_interface(self):
        """Создание пользовательского интерфейса"""
        # Главный фрейм
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Конфигурация веса строк и столбцов
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(0, weight=1)

        # Фрейм для графика
        graph_frame = ttk.Frame(main_frame)
        graph_frame.grid(row=0, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)

        # Создание компонентов
        self.plotter = Plotter(graph_frame)
        self.input_frame = InputFrame(main_frame, self.update_graphs)
        self.info_panel = InfoPanel(main_frame)

    def update_graphs(self):
        """Обновление графиков с новыми параметрами"""
        # Получаем параметры
        params = self.input_frame.get_parameters()

        # Создаем калькулятор функций с нужной точностью
        self.function_calculator = FunctionCalculator(params['epsilon'])

        # Генерируем данные
        x_values, y_values, z_values = self.function_calculator.generate_data(
            params['x_start'],
            params['x_end'],
            params['dx'],
            params['b']
        )

        # Обновляем графики
        self.plotter.update_plots(x_values, y_values, z_values, params['epsilon'], params['b'])


def main():
    """Главная функция запуска приложения"""
    root = tk.Tk()
    app = Lab8App(root)
    root.mainloop()


if __name__ == "__main__":
    main()