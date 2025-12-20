#лаб 1
from math import cos, sin


def lab1():
    # Чтение входных данных из файла
    with open('input.txt', 'r', encoding='utf-8') as f_in:
        lines = f_in.readlines()
        x = float()
        y = float()

        x, y = float(lines[0].strip())

    # Вычисление результатов
    z1 = cos(x) ** 4 + sin(y) ** 2 + 1 / 4 * sin(2 * x) - 1
    z2 = sin(y + x) * sin(y - x)
    print(z1, z2)

    # Запись результатов в файл
    with open('output.txt', 'w', encoding='utf-8') as f_out:
        f_out.write("Лабораторная работа 1\n")
        f_out.write("Результаты функций:\n")
        f_out.write(f"{z1}\n")
        f_out.write(f"{z2}\n")
#лаб 4
import random


def lab4():
    # Чтение входных данных из файла
    with open('input.txt', 'r', encoding='utf-8') as f_in:
        lines = f_in.readlines()
        n = int(lines[1].strip())  # вторая строка для lab4
        a = float(lines[2].strip())  # третья строка для lab4
        b = float(lines[3].strip())  # четвертая строка для lab4

    array = [round(random.uniform(-5, 5), 3) for _ in range(n)]

    max_element = max(array)

    last_positive_index = -1
    for i in range(len(array) - 1, -1, -1):
        if array[i] > 0:
            last_positive_index = i
            break

    sum_before = sum(array[:last_positive_index]) if last_positive_index != -1 else 0

    # Сжатие массива
    i = 0
    removed_count = 0
    while i < len(array):
        if a <= abs(array[i]) <= b:
            array.pop(i)
            removed_count += 1
        else:
            i += 1
    array.extend([0] * removed_count)

    # Запись результатов в файл
    with open('output.txt', 'a', encoding='utf-8') as f_out:
        f_out.write("\nЛабораторная работа 4\n")
        f_out.write(f"Массив до преобразования: {array}\n")
        f_out.write(f"Максимальный элемент: {max_element}\n")
        f_out.write(f"Сумма до последнего положительного: {sum_before}\n")
        f_out.write(f"Массив после преобразования: {array}\n")


#лаб 5

from random import uniform


def generate_matrix(size):
    matr = list()
    for i in range(0, size):
        matr.append(list())
        for j in range(0, size):
            matr[i].append(round(uniform(-10, 10), 2))
    return matr


def sum_el(matr):
    sum_total = 0
    results = []
    for i in range(0, len(matr)):
        flag = True
        buf = 0
        for j in range(0, len(matr)):
            if matr[j][i] < 0:
                flag = False
            buf += matr[j][i]
        if flag:
            sum_total += buf
            results.append((i, buf))
    return sum_total, results


def min_sum_dig(matr):
    n = len(matr)
    min_sum = float('inf')
    diagonal_info = []
    for k in range(0, 2 * n - 1):
        current_sum = 0
        for i in range(0, n):
            j = k - i
            if j >= 0 and j < n:
                current_sum += abs(matr[i][j])
        if current_sum < min_sum and current_sum > 0:
            min_sum = current_sum
        diagonal_info.append((k, current_sum))
    return min_sum, diagonal_info


def lab5():
    # Чтение входных данных из файла
    with open('input.txt', 'r', encoding='utf-8') as f_in:
        lines = f_in.readlines()
        n = int(lines[4].strip())  # пятая строка для lab5

    a = generate_matrix(n)

    sum_result, column_results = sum_el(a)
    min_result, diagonal_info = min_sum_dig(a)

    # Запись результатов в файл
    with open('output.txt', 'a', encoding='utf-8') as f_out:
        f_out.write("\nЛабораторная работа 5\n")
        f_out.write("Матрица:\n")
        for row in a:
            f_out.write(' '.join(f'{elem:7.2f}' for elem in row) + '\n')

        f_out.write("\n1. Сумма элементов в столбцах без отрицательных элементов:\n")
        for col, sum_val in column_results:
            f_out.write(f"Столбец {col}: сумма = {sum_val:.2f}\n")
        f_out.write(f"Общая сумма: {sum_result:.2f}\n")

        f_out.write("\n2. Минимум среди сумм модулей элементов диагоналей:\n")
        for k, sum_val in diagonal_info:
            f_out.write(f"Диагональ i+j={k}: сумма модулей = {sum_val:.2f}\n")
        f_out.write(f"Минимальная сумма: {min_result:.2f}\n")


def run_all_labs():
    # Очистка выходного файла перед записью
    with open('output.txt', 'w', encoding='utf-8') as f_out:
        f_out.write("Результаты выполнения лабораторных работ:\n")


    #lab1()
    lab4()
    lab5()

    print("Все лабораторные работы выполнены. Результаты записаны в output.txt")


if __name__ == "__main__":
    run_all_labs()