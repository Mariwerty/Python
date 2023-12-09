# cоздать итерируемый объект, возвращающий генератор тридцати пяти чисел трибоначчи и вывести эти числа

class Tribonacci:

    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        return self.generator()

    def generator(self):
        num1, num2, num3 = 0, 0, 1
        for i in range(0, self.limit):
            yield num1
            num1, num2, num3 = num2, num3, num1 + num2 + num3

tribonacci_iter = Tribonacci(35)
tribonacci_iter.generator()

for num in tribonacci_iter:
    print(num)
