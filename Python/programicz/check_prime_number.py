# prime number = 2,3,5,7,11,13,17,19......
number = int(input("Enter number : "))

flag = True
for i in range(2,number):
    if(number == 0 and number == 1):
        print("This is not a prime number")
    elif(number % i == 0):
        print(number,"is not a prime number")
        flag= False
        break
    
if flag == True:
    print(number,"is a prime number")
        
