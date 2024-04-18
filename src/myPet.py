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
    
    def age_in_months(self): 
        return 12*self.age
    
    def can_swim(self): 
        """Testing if the pet can swim or not. PWD's can swim, Manx cats cant"""
        can_swim = False 
        if self.breed == "PWD": 
            can_swim = True
        return can_swim

    def vocalize(self): 
        """Make the pet talk"""
        vocalization = ''
        if self.species == "Dog": 
            vocalization = "BARK"
        
        if self.species == "Cat":
            vocalization = "meow"
        return vocalization