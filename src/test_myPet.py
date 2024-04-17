import random 
from src.main import myPet

maggie = myPet(name="Maggie",
               species="Dog",
               breed="PWD",
               age=0.5,
               is_good=True)

def test_name():
    assert maggie.name == "Maggie"

def test_species(): 
    assert maggie.species == "Dog" 

def test_breed(): 
    assert maggie.breed == "PWD"

def test_age():
    assert maggie.age == 0.5

def test_is_good(): 
    assert maggie.is_good == True