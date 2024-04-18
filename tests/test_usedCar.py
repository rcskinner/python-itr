import unittest
from src.usedCar import usedCar

car = usedCar("Toyota", "Tacoma", 1997, 300E3, 20, 20)

class TestusedCarInit(unittest.TestCase): 

    def test_make(self): 
        self.assertEqual(car.make, "Toyota")
    
    def test_model(self): 
        self.assertEqual(car.model, "Tacoma")

    def test_year(self): 
        self.assertEqual(car.year, 1997)
    
    def test_mileage(self): 
        self.assertEqual(car.mileage, 300E3)

class TestusedCarMethods(unittest.TestCase): 

    def test_range_calculation(self):
        self.assertEqual(car.calculate_range(),20*20)
