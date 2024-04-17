import unittest
from src.main import usedCar

car = usedCar("Toyota", "Tacoma", 1997, 300E3)

class TestusedCarInit(unittest.TestCase): 

    def test_make(self): 
        self.assertEqual(car.make, "Toyota")
    
    def test_model(self): 
        self.assertEqual(car.model, "Toyota")

    def test_year(self): 
        self.assertEqual(car.year, 1997)
    
    def test_mileage(self): 
        self.assertEqual(car.mileage, 300E3)