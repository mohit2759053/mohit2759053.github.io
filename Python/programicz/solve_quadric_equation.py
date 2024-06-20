#import complex math module
import cmath

a= int(input("Enter a: \n"))

b= int(input("Enter b: \n"))

c= int(input("Enter c: \n"))

d= (b**2)-(4*a*c)

solution_1 = (-b-cmath.sqrt(d))/(2*a)

solution_2 = (-b+cmath.sqrt(d))/(2*a)

print("The solution are {0} and {1} ".format(solution_1,solution_2))