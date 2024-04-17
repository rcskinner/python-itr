
class usedCar(): 
    def __init__(self, make, model,year,mileage):
        self.make = make 
        self.model = model 
        self.year = year
        self.mileage = mileage

class myPet():
    def __init__(self, name, species, breed, age, is_good): 
        self.name = name
        self.species = species
        self.breed  = breed
        self.age = age
        self.is_good = is_good

    def has_tail(self): 
        """Function to check the myPet object to determine if the 
        pet has a tail."""
        has_tail = True
        if self.breed == "Manx": 
            has_tail = False
        return has_tail

if __name__ == 'main': 
    print ("Hello, World!")