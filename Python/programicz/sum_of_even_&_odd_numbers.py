a = int(input("enter number\n"))

even_sum = 0
odd_sum  = 0 

for i in range (1,a+1):
    if(i%2==0):
        even_sum = even_sum + i                
    else:
        odd_sum = odd_sum + i

print("the sum of even numbers 1 to {0}={1}" .format(i,even_sum))
    
print("The sum of odd numbers 1 to {0}={1}".format(i,odd_sum))
        



#making a program for check even numbers

a = int(input("ENTER NUMBER FOR SUM \n"))

sumofeven = 0
sumofodd  = 0

for i in range (1,a+1):
    if(i%2==0):
        sumofeven = sumofeven + i
    else:
        sumofodd = sumofodd + i
print("the sum of even numbers 1 to {0}={1}" .format(i,sumofeven))

print("the sum of odd numbers 1 to {0}={1}" .format(i,sumofodd))