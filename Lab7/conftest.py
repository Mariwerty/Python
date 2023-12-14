import pytest
from Lab5.Car_magic import Car


@pytest.fixture
def car1():
    return Car("Audi", "Q7", 2018, "white", 36000, "CA1058")


@pytest.fixture
def car2():
    return Car("Nissan", "Qashqai", 2018, "black", 20500, "EA6565")

