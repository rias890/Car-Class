
class Cars: 
    def __init__(self, make, model, year, price, used, mileage, doors, available):
        self.make= make 
        self.model = model
        self.year = year 
        self.__price = price 
        self.used = used 
        self.mileage = mileage 
        self.doors = doors 
        self.__available = available

        
    def stringify(e):
        print("The make of car is ", e.make)
        print("The model of the car is ", e.model)
        print("The year of the car is ", e.year)
        print("The price is ", e.__price)
        print("It is used? ", e.used)
        print("It's mileage is ", e.mileage)
        print("It has ", e.doors, " doors")
        print("Is it available? ", e.__available)
    
    def getAvailable(self):
        return self.__available
    
    def setAvailable(self, newavailable):
        self.__available = newavailable
        return self.__available
        
    def getPrice(self):
        return self.__price
    
    def setPrice(self, newprice): 
        self.__price = newprice 
        return self.__price 


class Motorcycle(Cars):
    def __init__(self, make, model, year, price, used, mileage, doors, available, type):
        super().__init__(make, model, year, price, used, mileage, doors, available)
        self.type = type
    def stringify(e):
        super().stringify()
        print("What type is it?", e.type)
    
        
class Truck(Cars):
    def __init__(self, make, model, year, price, used, mileage, doors, available, type, bedsize):
        super().__init__(make, model, year, price, used, mileage, doors, available)
        self.type = type 
        self.bedsize = bedsize
    def stringify(e):
        super().stringify()
        print("What type is it?", e.type)
        print("What bedsize is it?", e.bedsize)
        
    

    


  
