from Challenge65 import Cars
from Challenge65 import Motorcycle
from Challenge65 import Truck
fObj = open("DataofCars.txt")

carList = []
motorcyle = []
truck = []
counter = 0
currentLine = fObj.readlines()

while counter%9 == 0: 
    separate = currentLine[counter].split(":")
    make = separate[1]
    make = make.replace("\n", "") 
    make = make.replace(" ", "")
    counter = counter+1
    separate = currentLine[counter].split(":")
    
    model = separate[1]
    model = model.replace("\n", "")
    model = model.replace(" ", "")
    counter = counter+1
    separate = currentLine[counter].split(":")
   

    year = separate[1]
    year = year.replace("\n", "")
    year = year.replace(" ", "")
    counter = counter+1
    separate = currentLine[counter].split(":")
    

    price = separate[1]
    price = price.replace("\n", "")
    price = price.replace(" ", "")
    counter = counter+1
    separate = currentLine[counter].split(":")

    used = separate[1]
    used = used.replace("\n", "")
    used = used.replace(" ", "")
    counter = counter+1
    separate = currentLine[counter].split(":")

    mileage = separate[1]
    mileage = mileage.replace("\n", "")
    mileage = mileage.replace(" ", "")
    counter = counter+1
    separate = currentLine[counter].split(":")

    doors = separate[1]
    doors = doors.replace("\n", "")
    doors = doors.replace(" ", "")
    counter = counter+1
    separate = currentLine[counter].split(":")
    
    available = separate[1]
    available = available.replace("\n", "")
    available = available.replace(" ", "")
    separate = currentLine[counter].split(":")
    counter = counter+2
    

    
    eachcar = Cars (make, model, year, price, used, mileage, doors, available)
    carList.append(eachcar)
    

   
    if counter == 27:
        break
    

countertwo = 27
while countertwo == 27: 
    separate = currentLine[countertwo].split(":")
    make= separate[1]
    print(countertwo)
    make = make.replace("\n", "") 
    make = make.replace(" ", "")
    countertwo = countertwo+1
    separate = currentLine[countertwo].split(":")
    
    print(countertwo)
    model = separate[1]
    model = model.replace("\n", "")
    model = model.replace(" ", "")
    countertwo = countertwo+1
    separate = currentLine[countertwo].split(":")
    
    print(countertwo)
    year = separate[1]
    year = year.replace("\n", "")
    year = year.replace(" ", "")
    countertwo = countertwo+1
    separate = currentLine[countertwo].split(":")
    
    print(countertwo)
    price = separate[1]
    price = price.replace("\n", "")
    price = price.replace(" ", "")
    countertwo = countertwo+1
    separate = currentLine[countertwo].split(":")
    
    print(countertwo)
    used = separate[1]
    used = used.replace("\n", "")
    used = used.replace(" ", "")
    countertwo = countertwo+1
    separate = currentLine[countertwo].split(":")
    
    print(countertwo)
    mileage = separate[1]
    mileage = mileage.replace("\n", "")
    mileage = mileage.replace(" ", "")
    countertwo = countertwo+1
    separate = currentLine[countertwo].split(":")
    
    print(countertwo)
    doors = separate[1]
    doors = doors.replace("\n", "")
    doors = doors.replace(" ", "")
    countertwo = countertwo+1
    separate = currentLine[countertwo].split(":")
    
    print(countertwo)
    available = separate[1]
    available = available.replace("\n", "")
    available = available.replace(" ", "")
    countertwo = countertwo+1
    separate = currentLine[countertwo].split(":")
    
    
    print(countertwo)
    type = separate[1]
    type = type.replace("\n", "")
    type = type.replace(" ", "")
    countertwo = countertwo+1
    separate = currentLine[countertwo].split(":")
    
    
    onemotorcycle = Motorcycle(make, model, year, price, used, mileage, doors, available,type)
    carList.append(onemotorcycle)
    
 
    
    if countertwo == 36: 
        break
    
counterthree = 37

while counterthree==37:
    print(counterthree)
    separate = currentLine[counterthree].split(":")
    make = separate[1]
    make = make.replace("\n", "") 
    make = make.replace(" ", "")
    counterthree = counterthree+1
    separate = currentLine[counterthree].split(":")
    
    print(counterthree)
    model = separate[1]
    model = model.replace("\n", "")
    model = model.replace(" ", "")
    counterthree = counterthree+1
    separate = currentLine[counterthree].split(":")
    
    print(counterthree)
    year = separate[1]
    year = year.replace("\n", "")
    year = year.replace(" ", "")
    counterthree = counterthree+1
    separate = currentLine[counterthree].split(":")
    
    print(counterthree)
    price = separate[1]
    price = price.replace("\n", "")
    price = price.replace(" ", "")
    counterthree = counterthree+1
    separate = currentLine[counterthree].split(":")
    
    print(counterthree)
    used = separate[1]
    used = used.replace("\n", "")
    used = used.replace(" ", "")
    counterthree = counterthree+1
    separate = currentLine[counterthree].split(":")
    
    print(counterthree)
    mileage = separate[1]
    mileage = mileage.replace("\n", "")
    mileage = mileage.replace(" ", "")
    counterthree = counterthree+1
    separate = currentLine[counterthree].split(":")
    
    print(counterthree)
    doors = separate[1]
    doors = doors.replace("\n", "")
    doors = doors.replace(" ", "")
    counterthree = counterthree+1
    separate = currentLine[counterthree].split(":")
    
    print(counterthree)
    available = separate[1]
    available = available.replace("\n", "")
    available = available.replace(" ", "")
    counterthree = counterthree+1
    separate = currentLine[counterthree].split(":")
    
    
    print(counterthree)
    type = separate[1]
    type = type.replace("\n", "")
    type = type.replace(" ", "")
    counterthree = counterthree+1
    separate = currentLine[counterthree].split(":")
    
    print(counterthree)
    separate = currentLine[counterthree].split(":")
    bedsize = separate[1]
    bedsize = bedsize.replace("\n", "")
    bedsize = bedsize.replace(" ", "")
    counterthree = counterthree+1
    
    onetruck = Truck(make, model, year, price, used, mileage, doors, available,type, bedsize)
    carList.append(onetruck)

    if counterthree == 48: 
        break


for i in carList:
    print(i.stringify())
    
    #reading the wrong make for the mtorcyle and truck
   
       

print("1.Find a car using the model")

print("2. Add a car")

print("3. Mark the card sold and make it unavailable")

print("4. Change the mileage")


userinput = input("Select one of the options: ")


if userinput == "1": 
    whatcar = input("What car, motorcycle, or truck do you want to find? Toyota, Chevrolet, Honda, Suzuki, GMC: ")
    for e in carList:
        if whatcar == e.make:
            print(e.stringify())
            

if userinput == "2": 
    isnewcar= input("Do you want a car,motorcycle, or truck?")
    newmake = input("What make is it? ")
    newmodel = input("What model is it? ")
    newyear = input("What year is it? ")
    newprice = input("What price is it? ")
    newused = input("Is it used? ")
    newmileage = input("What is the mileage? ")
    newdoors = input("How many doors are there? ")
    newavailable= input("Is it available? ")
    
    if isnewcar == "car": 
        newitem = Cars(newmake,newmodel,newyear,Cars.setPrice(newprice),newused,newmileage, newdoors, Cars.setAvailable(newavailable))
        carList.append(newitem)
        print(carList)
        
    if isnewcar == "motorcycle": 
        newtype = input("What type is it? ")
        newitem = Motorcycle(newmake,newmodel,newyear,newprice,newused,newmileage, newdoors, newavailable, newtype)
        carList.append(newitem)
        print(carList)

    if isnewcar == "truck": 
        newtype = input("What type is it? ")
        newbedsize = input("What type of bedsize is it? ")
        newitem = Truck(newmake,newmodel,newyear,newprice,newused,newmileage, newdoors, newavailable, newtype, newbedsize)
        carList.append(newitem)
        print(carList)

    for i in carList:
        print(Cars.stringify(i))


if userinput == "3": 
    whatsold = input("Which car do you want to change the availability for? Toyota, Honda, Chevrolet, Suzuki, GMC:  ")
    for i in carList:
        if i.make == whatsold:
            if i.getAvailable == "TRUE":
                i.available = "FALSE"
            elif i.getAvailable == "FALSE":
                i.available = "TRUE"
            print(Cars.stringify(i))


if userinput == "4": 
    changemileage = input("Which car do you want to change the mileage for? Toyota, Honda, or Chevrolet, Suzuki, GMC: ")
    for w in carList: 
        if w.make == changemileage: 
            newmileage = input("Enter new mileage: ")
            w.mileage = newmileage
            print(Cars.stringify(w))



    


