num = int(input("Enter Number :\n"))

s=0
while(num > 0):                                             # suppose we are taking number 248 then 
   r=num%10                                             # here 248 % 10 = 8 , then s = 0 + 8 = 8 ; (24 % 10 = 4)- 8 + 4 = 12 ; (2 % 10 = 2 ) 12 + 2 => 14 
   s=s+r                                            
   num=num//10
print("Sum of digits is",s)
