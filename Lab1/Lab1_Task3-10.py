# 3-10.	Найти среднее арифметическое трех последних элементов списка.

import random
from statistics import mean

n = int(input("Введите длину списка: \n"))
A = [random.randint(0, 99) for i in range(n)]
print("Список: ")
print(A)

B = [A[n-3], A[n-2], A[n-1]]
avg_sum = mean(B)
print("Среднее арифметическое трех последних элементов списка равно: " + str(avg_sum))