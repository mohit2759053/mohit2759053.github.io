#calculate the sum of even numbers
sum=0
n=int(input("enter the even range to calculate sum"))
for i in range(2,11,2):
    sum=sum+i
    print(sum)

#calculate the sum of odd numbers
sum=0
n=int(input("enter the odd range to calculate sum"))
for i in range(1,11,2):
    sum=sum+i
    print(sum)