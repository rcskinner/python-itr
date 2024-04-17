import random
from src.main import usedCar

car = usedCar("Toyota", "Tacoma", 1997, 300E3)

def test_make(): 
    assert car.make == "Toyota"

def test_model(): 
    assert car.model == "Tacoma"

def test_year(): 
    assert car.year == 1997

def test_mileage(): 
    assert car.mileage == 300E3

def test_flaky_mileage(): 
    r = random.random()
    if r > 0.5: 
        car.mileage = 20E3 
    assert car.mileage == 300E3 