check = int(input("Enter Number : "))

if check > 1 :
    for i in range(2,check):
        if(check%i==0):
            print(check,"is not a prime number")
            break
        
    else:
        print(check,"is a prime number")

else:
    print(check,"is not prime number")