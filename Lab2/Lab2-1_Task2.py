# 2. Введите одномерный целочисленный список. Найдите наибольший нечетный элемент.
# Найдите минимальный по модулю элемент списка.
import random

n = int(input("Введите длину списка: \n"))
A = [random.randint(-99, 99) for i in range(n)]

min = A[0]
max = A[0]
print(A)

for i in range(len(A)):
    if abs(A[i] < abs(min)):
        min = abs(A[i])
    if A[i] > max and A[i] % 2 != 0:
        max = A[i]

print("Минимальное по модулю значение списка: ", min)
print("Максимальное нечетное значение списка = ", max)
