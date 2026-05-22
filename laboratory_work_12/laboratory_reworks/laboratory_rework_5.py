
"""
Модуль для лабораторной работы №5
Операции с матрицами: поиск столбцов без нулей и сортировка строк по характеристикам
"""

__all__ = [
    'input_matrix_dimensions',
    'input_matrix',
    'print_matrix',
    'count_columns_without_zeros',
    'calculate_row_characteristic',
    'sort_rows_by_characteristics',
    'get_row_characteristics',
    'print_row_characteristics',
    'main'
]


def input_matrix_dimensions() -> tuple:
    """
    Запрашивает у пользователя размеры матрицы

    Returns:
        кортеж (количество строк, количество столбцов)
    """
    while True:
        try:
            print("Запуск лабораторной работы №5...")
            rows = int(input("Введите количество строк матрицы: "))
            cols = int(input("Введите количество столбцов матрицы: "))
            if rows > 0 and cols > 0:
                return rows, cols
            else:
                print("Размеры должны быть положительными числами.")
        except ValueError:
            print("Пожалуйста, введите целые числа.")


def input_matrix(rows: int, cols: int) -> list:
    """
    Запрашивает у пользователя ввод элементов матрицы

    Args:
        rows: количество строк
        cols: количество столбцов

    Returns:
        матрица в виде списка списков
    """
    matrix = []
    print(f"\nВведите элементы матрицы {rows}x{cols}:")

    for i in range(rows):
        while True:
            try:
                row_input = input(f"Строка {i + 1} (через пробел): ")
                elements = list(map(int, row_input.split()))

                if len(elements) != cols:
                    print(f"Ошибка: нужно ввести ровно {cols} элементов")
                    continue

                matrix.append(elements)
                break
            except ValueError:
                print("Ошибка: введите целые числа, разделенные пробелами")

    return matrix


def print_matrix(matrix: list, title: str = "Матрица") -> None:
    """
    Выводит матрицу на экран

    Args:
        matrix: матрица для вывода
        title: заголовок перед выводом
    """
    print(f"\n{title}:")
    for row in matrix:
        print(" ".join(f"{elem:4}" for elem in row))
    print()


def count_columns_without_zeros(matrix: list) -> int:
    """
    Подсчитывает количество столбцов, не содержащих нулевых элементов

    Args:
        matrix: исходная матрица

    Returns:
        количество столбцов без нулей
    """
    if not matrix:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])

    count = 0
    for j in range(cols):
        has_zero = False
        for i in range(rows):
            if matrix[i][j] == 0:
                has_zero = True
                break
        if not has_zero:
            count += 1

    return count


def calculate_row_characteristic(row: list) -> int:
    """
    Вычисляет характеристику строки:
    сумма положительных четных элементов

    Args:
        row: строка матрицы

    Returns:
        характеристика строки
    """
    characteristic = 0
    for element in row:
        if element > 0 and element % 2 == 0:
            characteristic += element
    return characteristic


def sort_rows_by_characteristics(matrix: list) -> list:
    """
    Сортирует строки матрицы по характеристикам

    Args:
        matrix: исходная матрица

    Returns:
        новая матрица с отсортированными строками
    """
    # Создаем список кортежей (характеристика, строка)
    rows_with_characteristics = []
    for row in matrix:
        characteristic = calculate_row_characteristic(row)
        rows_with_characteristics.append((characteristic, row))

    # Сортируем по характеристике
    rows_with_characteristics.sort(key=lambda x: x[0])

    # Формируем новую матрицу из отсортированных строк
    sorted_matrix = [row for _, row in rows_with_characteristics]

    return sorted_matrix


def get_row_characteristics(matrix: list) -> list:
    """
    Возвращает список характеристик всех строк

    Args:
        matrix: матрица

    Returns:
        список характеристик строк
    """
    return [calculate_row_characteristic(row) for row in matrix]


def print_row_characteristics(matrix: list) -> None:
    """
    Выводит характеристики всех строк матрицы

    Args:
        matrix: матрица
    """
    print("\nХарактеристики строк (сумма положительных четных элементов):")
    for i, row in enumerate(matrix):
        characteristic = calculate_row_characteristic(row)
        print(f"Строка {i + 1}: {characteristic}")


def main() -> None:
    """Основная функция программы (полностью соответствует твоему коду)"""
    # Ввод размеров матрицы
    rows, cols = input_matrix_dimensions()

    # Ввод матрицы пользователем
    matrix = input_matrix(rows, cols)

    # Вывод исходной матрицы
    print_matrix(matrix, "Исходная матрица")

    # 1. Определение количества столбцов без нулевых элементов
    columns_without_zeros = count_columns_without_zeros(matrix)
    print(f"1. Количество столбцов без нулевых элементов: {columns_without_zeros}")

    # Вывод характеристик строк
    print_row_characteristics(matrix)

    # 2. Сортировка строк по характеристикам
    sorted_matrix = sort_rows_by_characteristics(matrix)

    # Вывод отсортированной матрицы
    print_matrix(sorted_matrix, "Матрица после сортировки строк по характеристикам")

    # Вывод характеристик отсортированных строк
    print_row_characteristics(sorted_matrix)
    print("Конец вывода")
    print("-------------------------------------------")
if __name__ == "__main__":
    main()
else:
    print("Модуль лабораторной работы №5 импортирован")
    print("-------------------------------------------")
    main()