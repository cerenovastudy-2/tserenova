def bucket_sort(arr):
    """
    Реализация блочной (корзинной) сортировки.
    """
    # 1. Определяем количество корзин (возьмем равное количеству элементов)
    num_buckets = len(arr)
    # Создаем пустые корзины
    buckets = [[] for _ in range(num_buckets)]

    # 2. Распределяем элементы по корзинам
    for value in arr:
        # Индекс корзины определяется пропорционально значению элемента
        index = int(value * num_buckets)  # Для чисел в диапазоне [0, 1)
        buckets[index].append(value)

    # 3. Сортируем каждую корзину индивидуально
    for bucket in buckets:
        bucket.sort()  # Используем встроенную сортировку (можно и вставками)

    # 4. Объединяем отсортированные корзины в исходный массив
    k = 0
    for bucket in buckets:
        for value in bucket:
            arr[k] = value
            k += 1
    return arr

# Демонстрация работы алгоритма
if __name__ == "__main__":
    # Пример с дробными числами от 0 до 1
    example_array = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
    print("Исходный массив:", example_array)
    sorted_array = bucket_sort(example_array)
    print("Отсортированный массив:", sorted_array)


# Блинная сортировка (Pancake Sort)
def pancake_sort(arr):
    """
    Реализация блинной сортировки.
    """
    n = len(arr)

    # Постепенно уменьшаем размер неотсортированной части
    for curr_size in range(n, 1, -1):
        # Находим индекс максимального элемента в неотсортированной части
        max_idx = arr.index(max(arr[:curr_size]))

        # Если максимальный элемент не в конце неотсортированной части
        if max_idx != curr_size - 1:
            # Переворачиваем до максимального элемента, чтобы он оказался первым
            if max_idx != 0:
                arr[:max_idx + 1] = reversed(arr[:max_idx + 1])
                print(f"Переворот до макс элемента: {arr}")

            # Переворачиваем всю неотсортированную часть, чтобы макс элемент оказался в конце
            arr[:curr_size] = reversed(arr[:curr_size])
            print(f"Переворот неотсортированной части: {arr}")

    return arr

# Демонстрация работы алгоритма
if __name__ == "__main__":
    example_array = [3, 1, 4, 2, 7, 5, 6]
    print("Исходный массив:", example_array)
    sorted_array = pancake_sort(example_array.copy())
    print("Отсортированный массив:", sorted_array)

#Сортировка бусинами (Bead Sort)
def bead_sort(arr):
    """
    Реализация сортировки бусинами (гравитационной сортировки).
    """
    # Проверяем, что все элементы неотрицательные целые числа
    if any(not isinstance(x, int) or x < 0 for x in arr):
        raise ValueError("Сортировка бусинами работает только с неотрицательными целыми числами")

    if not arr:
        return arr

    # Создаем "абак" - матрицу бусин
    max_val = max(arr)
    beads = [[0] * max_val for _ in range(len(arr))]

    # Расставляем бусины согласно значениям массива
    for i, value in enumerate(arr):
        for j in range(value):
            beads[i][j] = 1

    # Симуляция "падения" бусин под действием гравитации
    for j in range(max_val):
        # Считаем количество бусин в каждом столбце
        bead_count = sum(1 for i in range(len(arr)) if beads[i][j] == 1)

        # "Сбрасываем" все бусины в столбце
        for i in range(len(arr)):
            beads[i][j] = 0

#Поиск скачками (Jump Search)
import math

def jump_search(arr, x):
    """
    Реализация поиска скачками в отсортированном массиве.
    """
    n = len(arr)

    # Определяем размер прыжка
    step = int(math.sqrt(n))
    prev = 0

    # Прыжки вперед до нахождения блока, где может быть элемент
    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Линейный поиск в найденном блоке
    while arr[prev] < x:
        prev += 1
        if prev == min(step, n):
            return -1

    # Если элемент найден
    if arr[prev] == x:
        return prev

    return -1

# Демонстрация работы алгоритма
if __name__ == "__main__":
    sorted_array = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    target = 55
    print("Отсортированный массив:", sorted_array)
    print(f"Цель поиска: {target}")
    result = jump_search(sorted_array, target)
    if result != -1:
        print(f"Элемент найден на индексе: {result}")
    else:
        print("Элемент не найден в массиве.")

#Экспоненциальный поиск (Exponential Search)
def binary_search(arr, left, right, x):
    """
    Вспомогательная функция бинарного поиска.
    """
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def exponential_search(arr, x):
    """
    Реализация экспоненциального поиска.
    """
    n = len(arr)

    # Если элемент в начале массива
    if arr[0] == x:
        return 0

    # Экспоненциально увеличиваем границу
    i = 1
    while i < n and arr[i] <= x:
        i *= 2

    # Выполняем бинарный поиск в найденном диапазоне
    left = i // 2
    right = min(i, n - 1)
    return binary_search(arr, left, right, x)

# Демонстрация работы алгоритма
if __name__ == "__main__":
    sorted_array = [2, 3, 4, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    target = 35
    print("Отсортированный массив:", sorted_array)
    print(f"Цель поиска: {target}")
    result = exponential_search(sorted_array, target)
    if result != -1:
        print(f"Элемент найден на индексе: {result}")
    else:
        print("Элемент не найден в массиве.")


#Тернарный поиск (Ternary Search)
def ternary_search(arr, left, right, x):
    """
    Реализация тернарного поиска.
    """
    if right >= left:
        # Делим массив на три части
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        # Проверяем, не находятся ли искомые точки в разделителях
        if arr[mid1] == x:
            return mid1
        if arr[mid2] == x:
            return mid2

        # Определяем, в какой трети может находиться элемент
        if x < arr[mid1]:
            return ternary_search(arr, left, mid1 - 1, x)
        elif x > arr[mid2]:
            return ternary_search(arr, mid2 + 1, right, x)
        else:
            return ternary_search(arr, mid1 + 1, mid2 - 1, x)

    return -1

# Демонстрация работы алгоритма
if __name__ == "__main__":
    sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 6
    print("Отсортированный массив:", sorted_array)
    print(f"Цель поиска: {target}")
    result = ternary_search(sorted_array, 0, len(sorted_array) - 1, target)
    if result != -1:
        print(f"Элемент найден на индексе: {result}")
    else:
        print("Элемент не найден в массиве.")

