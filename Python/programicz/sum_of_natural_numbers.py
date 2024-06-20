#make a program for add all natural numbers
n = int(input("enter number"))
sum = 0
while(n>0):
    sum=n*(n+1)/2
    print(sum)
    break