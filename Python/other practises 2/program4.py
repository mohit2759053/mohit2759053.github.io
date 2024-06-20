#reverse string
def reverse_string(str):
	c=len(str)
	rev= " "

	while c>0:
		rev=rev+ str[c-1]
		c=c-1
	return rev
print("reverse of string is ",reverse_string("python"))		