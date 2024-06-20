# The fibonacci series is the integar sequence of 0,1,1,2,3,5,8,13,21........
n_terms = int(input("Enter Terms : "))

n1  =  0
n2  =  1
sum =  0

print("Fibonacci  series upto",n_terms)
if (n_terms <= 0):
    print("Please Enter a positive number")
else:
    while(sum < n_terms):
        print(n1,end=",")
        nth = n1 + n2  # This mean to say the nth term is equal to (n-1)th + (n-2)th term....
    
#update the values
    
        n1 = n2
        n2 = nth
        sum += 1
        