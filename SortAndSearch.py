#Сортировка пузырьком - Python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]
print("Исходный массив:", *arr)
bubble_sort(arr)
print("Отсортированный массив:", *arr)

#Сортировка Шелла (Shell Sort) - Python
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

#Быстрая сортировка (Quick Sort) - Python
  def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

#Линейный поиск (Linear Search) - Python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

##Поиск Фибоначчи (Fibonacci Search) - Python
def fibonacci_search(arr, x):
    n = len(arr)
    fib_m2, fib_m1, fib_m = 0, 1, 1
    while fib_m < n:
        fib_m2, fib_m1, fib_m = fib_m1, fib_m, fib_m1 + fib_m
    
    offset = -1
    while fib_m > 1:
        i = min(offset + fib_m2, n - 1)
        if arr[i] < x:
            fib_m, fib_m1, fib_m2 = fib_m1, fib_m2, fib_m1 - fib_m2
            offset = i
        elif arr[i] > x:
            fib_m, fib_m1, fib_m2 = fib_m2, fib_m1 - fib_m2, fib_m2 - (fib_m1 - fib_m2)
        else:
            return i
    return -1


