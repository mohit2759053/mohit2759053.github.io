"""
 
 printing even no from list  
 by using function and yield method

"""
def print_even(list1):     # generator object means itrable object 
    for i in list1 :       
        if i%2==0:
            yield i

list1 =[2,4,3,7,6,9]
print("original list is",list1)
print("even no is :")
for j in print_even(list1):
    print(j)
