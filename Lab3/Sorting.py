import random
import datetime
import prettytable  # пакет для таблицы
import matplotlib.pyplot as plt  # библиотека для графика


def BubbleSort(A):  # сортировка пузырьком
    for i in range(len(A)):  # i - счетчик проходов по списку
        for j in range(len(A) - 1 - i):  # j - текущая позиция при проходе по списку
            if A[j] > A[j + 1]:  # сравнение текущего элемента со следующим
                a = A[j]
                A[j] = A[j + 1]  # перестановка местами A[j] и A [j+1]
                A[j + 1] = a


def InsertionSort(A):  # сортировка вставками
    for i in range(1, len(A)):  # i - текущая позиция при проходе по списку
        t = A[i]  # A[i] - вставляемый элемент
        j = i  # j - позиция в отсортированной части списка
        while j > 0 and t < A[j - 1]:  # j - смещается справа налево, от больших к меньшим
            A[j] = A[
                j - 1]  # эл-ты отсортированной части, больше вставляемого уступают место – сдвигаются (копируются) вправо
            j -= 1  # j остановится на посл. эл-те, большем вставляемого
        A[j] = t  # вставляемый эл-т ставится на освободившееся место


def ShakerSort(A):  # шейкерная сортировка
    for i in range(len(A) // 2):  # i - счетчик пар проходов по списку, которых в 2 раза меньше, чем в пузырьковой
        for j in range(len(A) - 1 - i):  # j - номер позиции при проходе по списку слева направо
            if A[j] > A[j + 1]:  # сравнение текущего элемента со следующим
                a = A[j]
                A[j] = A[j + 1]
                A[j - 1] = a
        for j in range(len(A) - 2 - 1, i + 1, -1):  # j - номер позиции при проходе по списку справа налево
            if A[j] < A[j - 1]:  # сравнение текущего элемента с предыдущим
                a = A[j]
                A[j] = A[j - 1]
                A[j - 1] = a


def QuickSort(A, fst, lst):  # быстрая сортировка
    if fst >= lst:
        return

    # i, j = fst, lst
    pivot = A[fst]  # опорный элемент, первый элемент списка по умолчанию
    # pivot = A[random.randint(fst, lst)] - для random quick sort
    first_bigger = fst + 1
    while first_bigger <= lst:
        if A[first_bigger] >= pivot:
            break
        first_bigger += 1
    i = first_bigger + 1
    while i <= lst:
        if A[i] < pivot:
            A[i], A[first_bigger] = A[first_bigger], A[i]
            first_bigger += 1
        i += 1

    last_smaller = first_bigger - 1
    A[fst], A[last_smaller] = A[last_smaller], A[fst]
    QuickSort(A, fst, last_smaller - 1)
    QuickSort(A, first_bigger, lst)


# prettyTable - красивый вывод информации в таблицах
table = prettytable.PrettyTable(["Размер списка",
                                 "Время пузырьковой сортировки",
                                 "Время сортировки вставками",
                                 "Время шейкерной сортировки",
                                 "Время быстрой сортировки"])
x = []
y1 = []
y2 = []
y3 = []
y4 = []

# генерация разных списков: 5 списков с количеством от 1000 до 5000 включительно с шагом 1000
for N in range(1000, 5001, 1000):
    x.append(N)
    min = 1
    max = N
    A = []
    for i in range(N):
        A.append(int(round(random.random() * (max - min) + min)))  # преобразовываем знчение от random в int
        # выражение можно заменить на random.randint(какие значения использовать)
    #print(A)

    B = A.copy()  # копия списка A, которая отправляется на вторую сортировку
    C = A.copy()
    D = A.copy()

    # print(B)

    # BubbleSort(A)
    print("---")
    # print(A)
    #
    # InsertionSort(B)
    # print(B)
    #
    # ShakerSort(C)
    # print(C)
    #
    # QuickSort(D, 0, len(D)-1)
    # print(D)

    t1 = datetime.datetime.now()  # timestamp - время до сортировки
    BubbleSort(A)
    t2 = datetime.datetime.now()  # время после сортировки
    y1.append((t2 - t1).total_seconds())
    print("Шейкерная сортировка   " + str(N) + "   заняла   " + str((t2 - t1).total_seconds()) + "c")

    t3 = datetime.datetime.now()
    InsertionSort(B)
    t4 = datetime.datetime.now()
    y2.append((t4 - t3).total_seconds())
    print("Сортировка вставками   " + str(N) + "   заняла   " + str((t4 - t3).total_seconds()) + "c")

    t5 = datetime.datetime.now()
    ShakerSort(C)
    t6 = datetime.datetime.now()
    y3.append((t6 - t5).total_seconds())
    print("Шейкерная сортировка   " + str(N) + "   заняла   " + str((t6 - t5).total_seconds()) + "c")

    t7 = datetime.datetime.now()
    QuickSort(D, 0, len(D) - 1)
    t8 = datetime.datetime.now()
    y4.append((t8 - t7).total_seconds())
    print("Быстрая сортировка   " + str(N) + "   заняла   " + str((t8 - t7).total_seconds()) + "c")

    # заполняем таблицу
    table.add_row([str(N), str((t2 - t1).total_seconds()), str((t4 - t3).total_seconds()),
                   str((t6 - t5).total_seconds()), str((t8 - t7).total_seconds())])
print(table)

plt.plot(x, y1, "C0")  # x- количество элементов, y - время сортировки, С0 - код цвета (необязательно)
plt.plot(x, y2, "C1")
plt.plot(x, y3, "C2")
plt.plot(x, y4, "C3")

plt.show()
