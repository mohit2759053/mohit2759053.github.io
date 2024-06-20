print("Enter Numbers for operation")

a = float(input("Enter First Number :\n"))
b= float(input("Enter Second Number :\n"))

print("What operation do you wnat ?")

operation = input("Enter +, -, x or divide : ")

if operation == "+" :
    print(a,operation,b, "=", a+b)

elif operation == "-" :
    print(a,operation,b, "=", a-b)

elif operation == "x" :
    print(a,operation,b, "=", a*b)

elif operation == "/" :
    print(a,operation,b, "=", a/b)

else:
    print("Invalid operation")
