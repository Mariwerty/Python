# Реализуйте рекурсивную функцию нарезания прямоугольника с заданными пользователем сторонами a и b
# на квадраты с наибольшей возможной на каждом этапе стороной.
# Выведите длины ребер получаемых квадратов и кол-во полученных квадратов.

try:
    length = int(input("Введите длину прямоугольника: "))
    width = int(input("Введите ширину прямоугольника: "))
    # count - количество квадратов
    count = 0


    def divide_rect(length, width, count):
        if length > 0 and width > 0:
            if length == width:
                print(f"Последний квадрат со стороной: {length}")
                count += 1
                print(f"Количество возможных квадратов: {count}")
                return
            elif length < width:
                print(f"{count + 1}-й квадрат со стороной: {length}")
                count += 1
                return divide_rect(length, width - length, count)
            else:
                print(f"{count + 1}-й квадрат со стороной: {width}")
                count += 1
                return divide_rect(length - width, width, count)
        else:
            print("Вы ввели отрицательное число")

    divide_rect(length, width, count)

except ValueError:
    print("Вы ввели не целое число")
