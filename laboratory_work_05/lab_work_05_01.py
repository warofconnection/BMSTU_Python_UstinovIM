def main():

    # Запрос размеров матрицы у пользователя
    rows = get_positive_integer("Введите количество строк матрицы: ")
    cols = get_positive_integer("Введите количество столбцов матрицы: ")

    # Создание и заполнение матрицы
    matrix = create_matrix(rows, cols)

    print("\nИсходная матрица:")
    print_matrix(matrix)

    # Перестановка столбцов по характеристикам
    sorted_matrix = sort_columns_by_characteristic(matrix)

    print("\nМатрица после перестановки столбцов:")
    print_matrix(sorted_matrix)

    # Вычисление суммы элементов в столбцах с отрицательными элементами
    sum_result = sum_columns_with_negative_elements(matrix)

    print(f"\nСумма элементов в столбцах с отрицательными элементами: {sum_result}")


def get_positive_integer(prompt):

    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Число должно быть положительным!")
        except ValueError:
            print("Пожалуйста, введите целое число!")


def create_matrix(rows, cols):

    matrix = []
    print(f"\nВведите элементы матрицы {rows}x{cols}:")

    for i in range(rows):
        row = []
        for j in range(cols):
            # Математическая нумерация: строки и столбцы с 1
            element = get_integer(f"Элемент строки {i + 1}, столбца {j + 1}: ")
            row.append(element)
        matrix.append(row)

    return matrix


def get_integer(prompt):

    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Пожалуйста, введите целое число!")


def print_matrix(matrix):

    if not matrix:
        return

    rows = len(matrix)
    cols = len(matrix[0])

    print("     ", end="")
    for j in range(cols):
        print(f"{j + 1:6} ", end="")
    print()

    for i in range(rows):
        print(f"{i + 1:3}: ", end="")
        for j in range(cols):
            print(f"{matrix[i][j]:6} ", end="")
        print()



def calculate_column_characteristic(matrix, col_index):

    characteristic = 0
    for i in range(len(matrix)):
        element = matrix[i][col_index]
        # Проверяем, что элемент отрицательный и нечетный
        if element < 0 and element % 2 != 0:
            characteristic += abs(element)
    return characteristic


def sort_columns_by_characteristic(matrix):

    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    # Вычисляем характеристики для всех столбцов
    characteristics = []
    for j in range(cols):
        characteristic = calculate_column_characteristic(matrix, j)
        characteristics.append((j, characteristic))

    # Сортируем столбцы по характеристикам
    characteristics.sort(key=lambda x: x[1])

    # Создаем новую матрицу с переставленными столбцами
    sorted_matrix = []
    for i in range(rows):
        new_row = []
        for j, _ in characteristics:
            new_row.append(matrix[i][j])
        sorted_matrix.append(new_row)

    # Выводим характеристики столбцов (математическая нумерация)
    print("\nХарактеристики столбцов (столбец: характеристика):")
    for orig_index, char in characteristics:
        print(f"Столбец {orig_index + 1}: {char}")

    return sorted_matrix


def sum_columns_with_negative_elements(matrix):

    if not matrix:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    total_sum = 0

    print("\nСтолбцы с отрицательными элементами:")

    for j in range(cols):
        has_negative = False
        column_sum = 0

        # Проверяем, есть ли в столбце отрицательные элементы
        for i in range(rows):
            element = matrix[i][j]
            column_sum += element
            if element < 0:
                has_negative = True

        # Если в столбце есть отрицательные элементы, добавляем его сумму к общей
        if has_negative:
            print(f"Столбец {j + 1}: сумма = {column_sum}")
            total_sum += column_sum

    return total_sum


# Запуск программы
if __name__ == "__main__":
    main()