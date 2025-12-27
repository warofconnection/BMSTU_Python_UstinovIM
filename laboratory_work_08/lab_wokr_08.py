import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import math


class Lab8App:
    def __init__(self, root):
        self.root = root
        self.root.title("Лабораторная работа №8 - Графики функций")

        # Установка размеров окна (большая часть экрана)
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        window_width = int(screen_width * 0.8)
        window_height = int(screen_height * 0.8)

        self.root.geometry(f"{window_width}x{window_height}")

        # Параметры по умолчанию
        self.x_start = -3.0
        self.x_end = 3.0
        self.dx = 0.01
        self.epsilon = 1e-6
        self.b = 0.0

        self.create_widgets()
        self.plot_graphs()

    def create_widgets(self):
        # Главный фрейм
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Конфигурация веса строк и столбцов
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(0, weight=1)

        # Фрейм для графика
        self.graph_frame = ttk.Frame(main_frame)
        self.graph_frame.grid(row=0, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)

        # Панель управления
        control_frame = ttk.LabelFrame(main_frame, text="Параметры", padding="10")
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
                   command=self.update_graphs).grid(row=5, column=0, columnspan=2, pady=10)
        ttk.Button(control_frame, text="Выход",
                   command=self.root.quit).grid(row=6, column=0, columnspan=2, pady=5)

        # Информация о функциях
        info_frame = ttk.LabelFrame(main_frame, text="Функции", padding="10")
        info_frame.grid(row=0, column=3, rowspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)

        info_text = """y(x) = ∑ (-1)ⁿ·x²ⁿ/n!
    (ряд Тейлора)

z(x) = e^{-x²} + b

b - параметр, вводимый с клавиатуры"""

        ttk.Label(info_frame, text=info_text, justify=tk.LEFT).pack(padx=5, pady=5)

    def y_taylor(self, x, epsilon):
        """Вычисление y(x) с помощью ряда Тейлора с заданной точностью"""
        result = 0.0
        term = 1.0  # n=0: (-1)^0 * x^0 / 0! = 1
        n = 0

        while abs(term) > epsilon:
            result += term
            n += 1
            term = ((-1) ** n) * (x ** (2 * n)) / math.factorial(n)

        return result

    def z_function(self, x, b):
        """Вычисление z(x) = e^(-x^2) + b"""
        return math.exp(-x ** 2) + b

    def plot_graphs(self):
        # Создаем фигуру matplotlib
        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        self.ax.set_title("Графики функций y(x) и z(x)", fontsize=14, fontweight='bold')
        self.ax.set_xlabel("Ось X", fontsize=12)
        self.ax.set_ylabel("Ось Y", fontsize=12)
        self.ax.grid(True, alpha=0.3)

        # Добавляем легенду
        self.ax.legend()

        # Создаем холст Tkinter для matplotlib
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.graph_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def update_graphs(self):
        try:
            # Получаем значения из полей ввода
            self.b = float(self.b_entry.get())
            self.x_start = float(self.x_start_entry.get())
            self.x_end = float(self.x_end_entry.get())
            self.dx = float(self.dx_entry.get())
            self.epsilon = float(self.epsilon_entry.get())

            # Проверка корректности введенных данных
            if self.x_start >= self.x_end:
                messagebox.showerror("Ошибка", "X начальное должно быть меньше X конечного")
                return
            if self.dx <= 0:
                messagebox.showerror("Ошибка", "Шаг dx должен быть положительным")
                return
            if self.epsilon <= 0:
                messagebox.showerror("Ошибка", "Точность ε должна быть положительной")
                return

            # Генерируем данные
            x_values = np.arange(self.x_start, self.x_end + self.dx, self.dx)
            y_values = [self.y_taylor(x, self.epsilon) for x in x_values]
            z_values = [self.z_function(x, self.b) for x in x_values]

            # Очищаем предыдущий график
            self.ax.clear()

            # Строим новые графики
            self.ax.plot(x_values, y_values, 'b-', linewidth=2, label=f'y(x) (ряд Тейлора, ε={self.epsilon})')
            self.ax.plot(x_values, z_values, 'r-', linewidth=2, label=f'z(x) = e^(-x²) + {self.b}')

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

        except ValueError as e:
            messagebox.showerror("Ошибка ввода", "Пожалуйста, введите корректные числовые значения")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")


def main():
    root = tk.Tk()
    app = Lab8App(root)
    root.mainloop()


if __name__ == "__main__":
    main()