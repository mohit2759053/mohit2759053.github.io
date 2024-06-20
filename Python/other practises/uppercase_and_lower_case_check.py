def string_test(s):
    l = 0
    u = 0
    for i in s:
        if i.islower():
            l +=1
        elif i.isupper():
            u +=1
        else:
            pass

    print("original string is ",s)
    
    print("no of upper case in string is ",u)

    print("no of lower case in string is ",l)

string_test("Hello  Pyhton ")