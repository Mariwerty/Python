# 6. Дано натуральное трехзначное число n. Верно ли, что среди его цифр есть 0 или 9?

import random

num = str(random.randrange(100, 1000))
print('Случайное число: ', num)
print('Да верно' if '0' in num or '9' in num else 'Нет')

