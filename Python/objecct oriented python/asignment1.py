class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
        
    def area(self):
        return self.length * self.breadth
        
    def perimeter(self):
        return 2*(self.length + self.breadth)
        
myobject = Rectangle(10,20)

print("The area of Rectangle is %s" %(myobject.area()))

print("The Perimeter of Rectangel is %s" %(myobject.perimeter()))