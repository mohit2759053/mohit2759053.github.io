# OOP Exercise 1: Create a Vehicle class with max_speed and mileage instance attributes

class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        
ob = Vehicle(10,20)
print(ob.max_speed,ob.mileage)

