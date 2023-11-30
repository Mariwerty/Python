# 3. # Найдите сумму отрицательных элементов списка.
# Найдите сумму элементов списка между двумя первыми нулями. Если двух нулей нет в списке, то выведите ноль.

import random

# создаем список
A = []
for i in range(200):
    A.append(random.randint(-50, 100))
print(A)

# сумма отрицательных элементов списка
negativeSum = 0
for a in range(len(A)):
    if (A[a] < 0):
        negativeSum += A[a]
print(f"Сумма от отрицательных значений списка {negativeSum}")

# сумма элементов между двумя первыми нулями
try:
    sum = 0
    firstNull = A.index(0) #index - возвращает индекс первого элемента со значением x
    secondNull = A.index(0, firstNull + 1) #поиск начинается с первого найденного нуля ранее
    for a in range(firstNull, secondNull):
        sum += A[a]
    print(f"Сумма элементов списка между двумя первыми нулями {sum}")
except:
    print("Значений ноль нет")
