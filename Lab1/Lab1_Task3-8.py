# 8. Найти значение максимального элемента списка.

# import random
#
# length = int(input("Enter length: \n"))
#
# if length <=0:
#     print ("Length must be more than 0")
# else:
#     A = [random.randint(0, 99) for i in range(length)]
#     maximum = A[0]
#     for i in range(len(A)):
#         print("Element #" + str (i+1) + " is " + str(maximum))
#         if A[i] > maximum:
#             maximum = A[i]
#     print("Maximum is " + str(maximum))

from random import randrange
print("Введите размерность списка: ", end=' ')
numbers = [randrange(0, 10) for _ in range(int(input()))]
print("Исходный список: ", numbers)

print(f"Минимальное значение списка: {min(numbers)}")

for i in range(numbers.count(min(numbers))):
    numbers.remove(min(numbers))
print("Конечный список: ", numbers)