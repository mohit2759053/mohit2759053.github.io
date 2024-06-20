# 2017 is not a leap year
# 1900 is not a leap year
# 2012 is a leap year
# 2000 is a leap year

year = int(input("Enter year : "))

if (year % 4 == 0):
    if(year % 100 == 0):
        if(year % 400 == 0):
            print(year,"is a leap year")
             
        else:
            print(year,"is not a leap year")
    else:
        print(year,"is not a leap year")
else:
    print(year,"is not a leap year")
