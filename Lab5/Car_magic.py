# класс Car с 5 магическими методами
import datetime


class Car:
    # статическое поле
    __id = 1

# 1 - метод __init__(self, other) инициализатор класса с определенными атрибутами
    def __init__(self, brand, model, year, color, price, reg_number):
        # динамические поля
        self.__id = Car.__id
        Car.__id += 1  # увеличиваем количество при создании каждого объекта
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__color = color
        self.__price = price
        self.__reg_number = reg_number

# 2 - метод __str__(self) для строкового представления данных выводимых в print()
    def __str__(self):
        return f"ID: {self.__id} Model: {self.__brand} {self.__model} Year: {self.__year} " \
               f"Color: {self.__color} Price: {self.__price}$ Registration number: {self.__reg_number}"

# 3 - метод __getattr__(self, other) - при попытке доступа к несуществующему атрибуту
    def __getattr__(self, item):
        if item == "full_price":
            return self.full_price
        else:
            print(f"Атрибута {item} не существует!")
            raise AttributeError

# 4 - метод __setattr__(self, other) - устанавливаем атрибуты объекта
    def __setattr__(self, key, value):
        if key == "full_price":
            self.__dict__[key] = self.__price * value
        else:
            self.__dict__[key] = value

# 5 - метод __eq__(self, other) - сравнивает объекты по выбранному атрибуту
    def __eq__(self, other):
        if isinstance(other, Car):
            return self.__year == other.year
        return False

    # метод класса
    # аргументом является класс (cls), а не объект, т.е. метод можно вызвать у самого класса
    # используется для операций, которые связаны с классом в целом, а не с отдельным объектом
    # могут изменять состояние всех объектов класса, но отдельный объект - нет
    @classmethod  # считаем количество объектов
    def get_id_counter(cls):
        return cls.__id

    # методы для записи и считывания инкапсулированных (private) атрибутов c проверкой вводимых значений
    def get_brand(self):
        return self.__brand

    def set_brand(self, my_brand):
        if isinstance(my_brand, str):
            self.__brand = my_brand

    def get_model(self):
        return self.__model

    def set_model(self, my_model):
        if isinstance(my_model, str):
            self.__model = my_model

    def get_year(self):
        return self.__year

    def set_year(self, year):
        if year > 1900:
            self.__year = year
        else:
            print("Please check the car's year of production")

    def get_color(self):
        return self.__color

    def set_model(self, my_color):
        if isinstance(my_color, str):
            self.__color = my_color

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("The price of the car shouldn't be less or equal to 0")

    def get_reg_number(self):
        return self.__reg_number

    def set_model(self, my_reg_number):
        if isinstance(my_reg_number, str):
            self.__reg_number = my_reg_number

    # статический метод
    # можно вызывать, обращаясь к имени класса, а не отдельному объекту (его можно и не создавать)
    # не используется self

    # подсчет возраста машины
    @staticmethod
    def calculate_car_age(car):
        current_year = datetime.datetime.now().year
        return current_year - car.__year

    # вывод автомобилей заданной марки
    def car_list_by_brand(brand):
        print(f"Cars of brand {brand}:")
        for car in cars:
            if car.__brand == brand:
                print(car)

    # вывод автомобилей заданной модели, которые экспуатируются больше n лет
    def filter_cars_by_model_and_age(cars, model, n):
        print(f"Cars of model {model} older than {n} years: ")
        for car in cars:
            if car.get_model() == model and Car.calculate_car_age(car) > n:
                print(car)

        # filtered_cars = [car for car in cars if car.get_model() == model and Car.calculate_car_age(car) > n]
        # print(f"Cars of model {model} older that {n} years: ")
        # for car in filtered_cars:
        #     print(car)

# создаем список объектов
cars = [
    Car("Audi", "A7", 2017, "grey", 25000, "HA1212"),
    Car("Audi", "Q7", 2018, "white", 36000, "CA1058"),
    Car("BMW", "X6", 2021, "black", 42000, "KH4858"),
    Car("Lexus", "RX", 2022, "grey", 51000, "OT5872"),
    Car("Mazda", "CX5", 2019, "red", 27000, "BA8596"),
    Car("Nissan", "Juke", 2013, "red", 12000, "PB5874"),
    Car("Nissan", "Qashqai", 2018, "black", 20500, "EA6565"),
    Car("Nissan", "Qashqai", 2012, "red", 11000, "PT8552"),
    Car("Porshe", "Cayenne", 2020, "blue", 78000, "CE7412"),
    Car("Tesla", "Model X", 2019, "white", 33000, "KM9632"),
    Car("Toyota", "Camry", 2017, "black", 24000, "MH5698"),
    Car("Volkswagen", "Tiguan", 2016, "white", 28000, "TK4853")
]
# через заданные значения
Car.car_list_by_brand("Audi")
Car.filter_cars_by_model_and_age(cars, "Qashqai", 4)

# через уточнения данных у пользователя
req1 = input("Введите наименование марки автомобиля: ")
Car.car_list_by_brand(req1)
req2 = input("Введите название модели автомобиля: ")
req3 = int(input("и приемлемый минимум лет: "))
Car.filter_cars_by_model_and_age(cars, req2, req3)
