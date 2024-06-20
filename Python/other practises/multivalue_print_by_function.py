#return many values by one function 
def fun():
    '''return 1      #this will never work properly,,,,, its output come =>     1     only on   
    return 2
    return 3'''
    
    return 1,2,3         #this will work because it has become a tuple

print(fun())

