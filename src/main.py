
class usedCar(): 
    def __init__(self, make, model,year,mileage, mpg, capacity):
        self.make = make 
        self.model = model 
        self.year = year
        self.mileage = mileage
        self.mpg = mpg 
        self.capacity = capacity

    def calculate_range(self): 
        range = self.capacity * self.mpg
        return range
    
    def miles_per_year(self): 
        mi_per_year = self.mileage / (2024 - self.year)
        return mi_per_year


if __name__ == 'main': 
    print ("Hello, World!")