lst=[]
num=int(input("How many number:\n"))

for i in range(num):
    numbers=int(input(("Enter number ")))
    lst.append(numbers)

print("Greatest element in the list is :",max(lst))
print("Smallest element in the list is :",min(lst))
