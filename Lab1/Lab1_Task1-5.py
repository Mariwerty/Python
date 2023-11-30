# 5. Определить, есть ли среди заданных целых чисел A, B, C, D хотя бы одно нечётное.

A = [int(input("Введите число A: \n")),
     int(input("Введите число B: \n")),
     int(input("Введите число C: \n")),
     int(input("Введите число D: \n"))]

count = 0

for i in range(len(A)):
    if A[i] % 2 != 0:
        print("Число ", A[i], "нечетное")
        count +=1
if count == 0:
    print("Все числа четные")

