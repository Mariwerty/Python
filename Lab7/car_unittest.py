import unittest
from Lab5.Car_magic import Car


class CarTest(unittest.TestCase):
    def setUp(self):
        self.car1 = Car("Audi", "Q7", 2018, "white", 36000, "CA1058")
        self.car2 = Car("BMW", "X6", 2021, "black", 42000, "KH4858")
        self.car3 = Car("Nissan", "Qashqai", 2018, "black", 20500, "EA6565")

    def testGetBrand(self):
        self.assertEqual(self.car1.get_brand(), "Audi")
        self.assertEqual(self.car2.get_brand(), "BMW")

    def testSetBrand(self):
        self.assertEqual(self.car1.get_brand(), "Audi")
        self.car1.set_brand("BMW")
        self.assertEqual(self.car1.get_brand(), "BMW")

    def testGetModel(self):
        self.assertEqual(self.car1.get_model(), "Q7")
        self.assertEqual(self.car2.get_model(), "X6")

    def testCalculateCarAge(self):
        self.assertEqual(Car.calculate_car_age(self.car1), 5)
        self.assertEqual(Car.calculate_car_age(self.car2), 2)

    def testEq(self):
        self.assertTrue(self.car1.get_year() == self.car3.get_year())

    def tearDown(self):
        del self.car1
        del self.car2
        del self.car3


if __name__ == '__main__':
    unittest.main()
