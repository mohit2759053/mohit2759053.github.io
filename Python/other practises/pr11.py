#table for any number which you want
num=int(input("Enter any number for make the table\n"))
for i in range(1,11):
	#print(str(num)+" x "+str(i)+" = "+str(i*num))   this can be also use
	print(f"{num}X{i}={num*i}")