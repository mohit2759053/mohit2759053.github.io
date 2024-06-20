#Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() 
# a default value of 50.

class Vehicle:
    def __init__(self,mileage,max_speed):
        self.mileage = mileage
        self.max_speed = max_speed 

    def seating_capacity(self,capacity):
        self.capacity = seating_capacity
        

class Bus(Vehicle):
    def seating_capacity(self,capacity=50):
        self.capacity = seating_capacity
            
        
object = Bus(20,23)
ob = Vehicle(2)
print(object.capacity)
print(ob.capacity)
        
    
