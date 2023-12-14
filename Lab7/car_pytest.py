def test_get_brand(car1):
    assert car1.get_brand() == "Audi"


def test_set_brand(car1):
    assert car1.get_brand() == "Audi"
    car1.set_brand("BMW")
    assert car1.get_brand() == "BMW"


def test_get_model(car2):
    assert car2.get_model() == "Qashqai"


def test_calculate_car_age(car1):
    assert car1.calculate_car_age(car1) == 5


def test__eq__(car1, car2):
    assert car1.get_year() == car2.get_year()


