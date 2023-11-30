# 5. Найдите наименьший четный элемент списка. Если такого нет, то выведите первый элемент.
# Преобразовать список так, чтобы сначала шли нулевые элементы, а затем все остальные.

import random

#создание списка
list_length = 10
init_list = [random.randint(0, 30) for i in range(list_length)]
print(f"Исходный список: {init_list}")

#наименьший четный элемент списка
min_value = init_list[0]
for i in range(1, len(init_list)):
    if i % 2 == 0:
        if init_list[i] < min_value:
            min_value = init_list[i]
print(f"Наименьший четный элемент списка: {min_value}")

#новый список с нулевыми элементами впереди
new_list = []
for a in range(len(init_list)):
    if init_list[a] == 0:
        new_list.append(init_list[a])
for b in range(len(init_list)):
    if init_list[b] != 0:
        new_list.append(init_list[b])
print(f"Новый список с нулевыми элементами вначале: {new_list}")