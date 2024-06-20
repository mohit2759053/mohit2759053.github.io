def dictionary_test(s):
    d={"l":0,"u":0}
    for i in s:
        if i.islower():
            d["l"]+=1 #l=l+1
        elif i.isupper():
            d["l"]+=1 #u=u+1
        else:
            pass

    print("original string is ",s)
    
    print("no of upper case in dictionary is ",d["u"])

    print("no of lower case in dictionary is ",d["l"])

dictionary_test("Hello;;;Pyhton")