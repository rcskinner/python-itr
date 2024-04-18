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

    def calculate_size(self): 
        if self.model == "Tacoma": 
            size = "M"
        return size

