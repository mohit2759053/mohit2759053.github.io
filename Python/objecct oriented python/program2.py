# Types  of Inheritance

# 1.Single Inheritance

# 2.Multiple Inheritance        

# 3.Multi level Inheritance


class Animal:
    def sleep(self):
        print("animal is sleeping")
    
class Dog(Animal):
    def bark(self):
        print("dog is barking")

class Dogchild(Dog):
    def eat(self):
        print("Dog child is eating")
        
d = Dogchild()
d.eat()
d.bark()
d.sleep()
    
    
# 4. Herarical Inheritance:
class Animal:
    def sleep(self):
        print("animal is sleeping")
    
class Dog(Animal):
    def bark(self):
        print("dog is  barking")

class Cat(Animal):
    def meow(self):
        print("cat is eating")

c = Cat()
c.sleep()
c.meow()