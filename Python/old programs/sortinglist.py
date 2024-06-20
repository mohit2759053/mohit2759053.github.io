#sorting the elements

lst=[]
number=int(input("enter no of element in list "))
print("enter elements in list ")
for i in range(number):
    element=int(input())
    lst.append(element)

swapping=True
while swapping:
    swapping = False

    for i in range(len(lst)-1):
        if not(lst[i]<lst[i+1]):
            lst[i],lst[i+1]=lst[i+1],lst[i]
            swapping=True

print("sorted list is here ",lst)