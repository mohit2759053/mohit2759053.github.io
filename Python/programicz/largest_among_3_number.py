a = int(input("Enter 1st Number : \n"))
b = int(input("Enter 2nd Number : \n"))
c = int(input("Enter 3rd Number : \n"))


if(a>=b) and (a>=c):
    largest = a
elif(b>=a) and (b>=c):
    largest = b
else:
    largest = c
print("The Largest Number is : ",largest)