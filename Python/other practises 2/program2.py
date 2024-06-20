# greatest among three numbers through function
def max_of_two(a,b,c):
    if a>b and a>c :
        return a 
    elif b>c:
        return b    
    return c

print(max_of_two(5,9,13))