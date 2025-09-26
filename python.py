#Массив
#Список (динамический массив)
dynamic_arr = [1, 2, 3, 4, 5]

#Добавление элемента
dynamic_arr.append(6)

#Доступ к элементам
print(f"Element at index 2: {dynamic_arr[2]}")

#Размер массива
print(f"Array size: {len(dynamic_arr)}")

#Срезы
print(f"Slice[1:4]: {dynamic_arr[1:4]}")

#Стеки

#Исльзование списка как стека
stack = []

#Добавление элемента
stack.append(1)
stack.append(2)
stack.append(3)

#Просмотр верхнего элемента
print(f"Top element: {stack[-1]}")

#Удаление элемента
stack.pop()

#Проверка на пустоту
ptint(f"Is empty: {len(stack) == 0}")

#Размер стека
print(f"Stack size: {len(stack)}")

