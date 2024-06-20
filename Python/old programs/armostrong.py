#armostrong number
num= int(input("enter number to check,that is armostrong or not "))
temp=num
total=0
while(num!=0):
    rem=num%10
    total = total + rem **3
    num=num//10

if(total==temp):
    print("Armostrong")
else:
    print("Not Armostrong")