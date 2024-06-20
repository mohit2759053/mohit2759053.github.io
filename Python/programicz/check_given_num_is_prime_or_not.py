a= int(input("Enter Number\n"))
prime_num=True

for i in range(2,a):
        
    if(a%2==0):
        prime_num=False
        break

if( a==0 | a==1 ):
    print("Given Number is not Prime")

elif (prime_num):
        print("Given Number is Prime")
else:
        print("Given Number is not prime")


    
