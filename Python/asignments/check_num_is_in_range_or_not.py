#python function to check whether given number is in range or not
range_1 = range(5,50)

number = int(input('Enter a number : '))
 
if number not in range_1 :
    print(number, 'is not present in the range.')
else :
    print(number, 'is present in the range.')
    
    