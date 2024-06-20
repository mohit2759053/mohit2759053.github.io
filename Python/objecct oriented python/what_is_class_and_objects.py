"""

OOP in python -

In Python, object-oriented Programming (OOPs) is a programming paradigm(means => example) that uses objects 
and classes in programming. It aims to implement real-world entities like inheritance, polymorphisms, 
encapsulation, etc.in the programming. The main concept of OOPs is to bind the data and the functions 
"that work on that together as a single unit so that no other part of the code can access this data."
(us par kaam ek saath ek unit ke jaise taaki code ka koi any part iss data tak nahin pahunch sake) 

python is a object oriented programming language.Unlike procedure oriented programming, where the main 
emphasis is on functions;object oriented programming stresses on objects.


Main Concepts of Object-Oriented Programming (OOPs): 

1.Class
2.Objects
3.Polymorphism*
4.Encapsulation*
5.Inheritance*

also

6.astraction*


1) Class ::: A class is a blueprint for the object.
We can think of class as a sketch(prototype or blueprint) of a house.It contains all the details about 
the floors, doors,windows etc. Based on these descriptions,we build the house.House is the object.
As many houses can be made from a descriptions, we can create many objects form a class.
An object is also called an instance of a class and the process of creating this object is called 
instantiation.

2) object ::: The object is an entity that has a state and behavior associated with it. It may be any 
real-world object like a mouse, keyboard, chair, table, pen, etc. Integers, strings, floating-point 
numbers, even arrays, and dictionaries, are all objects. More specifically, any single integer or any
single string is an object. The number 12 is an object, the string “Hello, world” is an object, a list
is an object that can hold other objects, and so on. You’ve been using objects all along and may not 
even realize it.


An object consists of :

State: It is represented by the attributes of an object. It also reflects the properties of an object.

Behavior: It is represented by the methods of an object. It also reflects the response of an object to other objects.

Identity: It gives a unique name to an object and enables one object to interact with other objects.
To understand the state, behavior, and identity let us take the example of the class dog (explained above). 


*The identity can be considered as the name of the dog.

*State or Attributes can be considered as the breed, age, or color of the dog.

T&he behavior can be considered as to whether the dog is eating or sleeping.
  """


#Example

class House:
    #methods and attributes
    pass

villa1 = House()
villa2 = House()
villa3 = House()
villaN = House()            #you can make unlimited instances or objects



# A class usually contains attrubutes(data and functions).For Example,

class MyClass:
    a=10
    def func(self):             #method 
        return "Hello"          

ob = Myclass()    # instantiate an object
print(ob.func())  # Output: Hello
print(ob.a)       # Output:10


'''
*Method :::

Methods are functions defined inside the body of a class. They are used to define the behaviors of an object.



*Self :::

Class methods must have an extra first parameter in the method definition. We do not give a value for this 
parameter when we call the method, Python provides it

If we have a method that takes no arguments, then we still have to have one argument.

This is similar to this pointer in C++ and this reference in Java.



The __init__ method :::


The __init__ method is similar to constructors in C++ and Java. It is run as soon as an object of a class 
is instantiated. The method is useful to do any initialization you want to do with your object. 

Now let us define a class and create some objects using the self and __init__ method.

'''

#Example

class Dog:
    class attribute
	    attr1 = "mammal"

	# Instance attribute
	def __init__(self, name):               #here is the __init__() method or also called as constructer
		self.name = name                        #you can use anything as the place of self

# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))

# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))


# Output

'''
Rodger is a mammal
Tommy is also a mammal
My name is Rodger
My name is Tommy
'''


'''
3)Inheritance :::
Inheritance is the capability of one class to derive or inherit the properties from another class. The class 
that derives properties(newly formed class) is called the derived class,sub class or child class and the class 
from which the properties are being derived(existing) is called the base class or parent class. 
In easy word you can understand:Inheritance is a way of creating a new class for using details of an existing
class without modifying it. The newly formed class is a derived class (or child class). Similarly, the 
existing class is a base class (or parent class).

The benefits of inheritance are:

1.It represents real-world relationships well.

2.It provides the reusability of a code. We don’t have to write the same code again and again. Also, it allows 
us to add more features to a class without modifying it.

3.It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses
of B would automatically inherit from class A.

Example: Inheritance in Python
'''

# parent class
class Bird:
    
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()

#output

# Bird is ready
# Penguin is ready
# Penguin
# Swim faster
# Run faster

'''
4).Polymorphism :::
Polymorphism simply means having many forms. For example, we need to determine if the given species of birds fly 
or not, using polymorphism we can do this using a single function.

'''
#Example:
#you can see here in every class we have make a common method(flight) and it will work 100% so this attribute is called pollymorphism
class Bird:
    	
	def intro(self):
		print("There are many types of birds.")

	def flight(self):
		print("Most of the birds can fly but some cannot.")

class sparrow(Bird):
	
	def flight(self):
		print("Sparrows can fly.")

class ostrich(Bird):

	def flight(self):
		print("Ostriches cannot fly.")

obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()

#output

# here are many types of birds.
# Most of the birds can fly but some cannot.
# There are many types of birds.
# Sparrows can fly.
# There are many types of birds.
# Ostriches cannot fly.

'''
5)Encapsulation :::
Using OOP in Python, we can restrict access to methods and variables. This prevents data from direct
modification which is called encapsulation. In Python, we denote private attributes using underscore 
as the prefix i.e single _ or double __.
'''

#Example

class Computer:
    
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()

#output

# Selling Price: 900
# Selling Price: 900
# Selling Price: 1000    by using setter function 

'''
In the above program, we defined a Computer class.

We used __init__() method to store the maximum selling price of Computer. We tried to modify the price. 
However, we can't change it because Python treats the __maxprice as private attributes.

As shown, to change the value, we have to use a setter function i.e setMaxPrice() which takes price
as a parameter.
'''

"""
Key Points to Remember:

1.Object-Oriented Programming makes the program easy to understand as well as efficient.

2.Since the class is sharable, the code can be reused.

3.Data is safe and secure with data abstraction.

4.Polymorphism allows the same interface for different objects, so programmers can write 
efficient code.

"""