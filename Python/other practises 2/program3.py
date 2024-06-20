#reverse number
n=int(input("enter no for reverse the numbmer"))
def reverse_no(num):
	rev=0
	while(num!=0):
		rem=num%10
		rev=rev*10+rem
		num=num//10
	return rev
print( reverse_no(n))		