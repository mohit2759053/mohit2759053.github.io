# program to find the numbers which are devisble by 7 and multiple of 5
nl=[]
for x in range(1500, 2701):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print (','.join(nl))  # this is used because the we need the result without any list
                       # but if you type  => print(n1) then output will look like
                       # ['1505','1540',_______,'2695']
