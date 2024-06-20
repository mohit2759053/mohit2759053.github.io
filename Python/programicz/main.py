# when the user enters negative number , the break statement is executed which terminates the loop
sum = 0
while True:
    n= input("Enter a number:\n")
    n= float(n)  #converting to float
    
    if n < 0: # check if number is negative
        break
    sum += n
    
    print("sum = ",sum)