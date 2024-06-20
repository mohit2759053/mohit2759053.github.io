#make a program for check that, given number is palindrome or not?
#palindrome means 161 is palindrome but 162 is not means number=reverse of number
#161=161(after rev)  but   162 = 261(rev) is not equal

a=int(input("Enter number\n"))
temp=a
rev=0
while(a>0):
    b=a%10
    rev=rev*10+b
    a=a//10
if(temp==rev):
    print("This a palindrome number")
else:
    print("This is not a palindrome number")