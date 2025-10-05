def main():
    # Ввод размера массива
    n = int(input("Введите размер массива: "))
    arr = []

    # Заполнение массива элементами
    for i in range(n):
        arr.append(float(input(f"Введите элемент {i + 1}: ")))

    # 1. Поиск номера минимального элемента
    min_index = arr.index(min(arr))
    print(f"Номер минимального элемента: {min_index + 1}")

    # 2. Поиск индексов первого и второго отрицательных элементов
    first_neg = None
    second_neg = None

    for idx, value in enumerate(arr):
        if value < 0:
            if first_neg is None:
                first_neg = idx
            elif second_neg is None:
                second_neg = idx
                break  # Выход после нахождения второго отрицательного

    # Вычисление суммы между отрицательными элементами
    total = 0
    if first_neg is not None and second_neg is not None:
        # Суммируем элементы между первым и вторым отрицательными
        total = sum(arr[first_neg + 1:second_neg])
    print(f"Сумма между первым и вторым отрицательными: {total}")

    # 3. Разделение массива по модулю
    left = [x for x in arr if abs(x) <= 1]  # Элементы с модулем <= 1
    right = [x for x in arr if abs(x) > 1]  # Элементы с модулем > 1
    sorted_arr = left + right  # Объединение списков

    print("Преобразованный массив:")
    print(sorted_arr)


if __name__ == "__main__":
    main()