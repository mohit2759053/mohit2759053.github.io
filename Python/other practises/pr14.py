lst=[]
num=int(input("Enter numbers in list "))
print("Enter number ")
element=0

for i in range(num):
    element=int(input())
    lst.append(element)
x=int(input("check number in list "))
for i in range(len(lst)):
    if(element == lst[i]):
        print("number exist in list and its index is ", i)
    