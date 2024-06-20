#program to find the area of triangle
a = float(input("Enter first side: \n"))
b = float(input("Enter second side: \n"))
c= float(input("Enter third side: \n"))

s = (a + b + c) / 2

area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

print("the area is %0.2f" %area)
