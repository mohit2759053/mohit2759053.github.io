#program for fibonacci series:
num= int(input("Enter the range for print fibonacci number: "))
firnum, secnum ,tempnum = 0, 1, 0

print(firnum)
print(secnum)
tempnum = firnum + secnum

while(tempnum<num):
    print(tempnum)
    firnum = secnum
    secnum = tempnum
    tempnum = firnum + secnum




