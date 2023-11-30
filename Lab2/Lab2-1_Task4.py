# 4. Найдите произведение элементов списка с нечетными номерами.
# Найдите наибольший элемент списка, затем удалите его и выведите новый список.

import random

#создание списка
list_length = int(input("Введите длину списка: \n"))
init_list = [random.randint(1, 30) for i in range(list_length)]
print(f"Исходный список: {init_list}")

#произведение элементов с нечетными номерами
mult = 1
for i in range(len(init_list)):
    if i % 2 != 0:
        mult *= init_list[i]
print(f"Произведение элементов списка с нечетными номерами: {mult}")

# найти наибольший элемент списка, затем удалить его и вывести новый список
max_elem = max(init_list)
print(f"Наибольший элемент списка: {max_elem}")
init_list.remove(max_elem)
print(f"Новый список: {init_list}")


