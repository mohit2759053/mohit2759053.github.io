#n! = 1 x 2 x 3 x 4 x 5.....x n
#! = 1 x 2 x 3 x 4 x 5 x 6 x 7 x 8 x 9 x 10 

num= int(input("Enter number for factorial "))
factorial = 1
for i in range(1,num+1):
    factorial = factorial * i
print(f"factorial of {num} is {factorial}")

