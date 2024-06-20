#calculate the sum of odd numbers from 2 to n numbers
sum=0
n=int(input("enter the odd range to calculate sum"))
for i in range(1,n+1,2):
    sum=sum+i
    print(sum)

#calculate the sum of even numbers from 1 to n numbers
sum=0
n=int(input("enter the even range to calculate sum"))
for i in range(2,n+1,2):
    sum=sum+i
    print(sum)