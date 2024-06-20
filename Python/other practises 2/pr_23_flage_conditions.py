text= input("Enter text here\n")

if("make money" or "Make money" in text):
    spam=True
elif("play games" in text):
    spam=True
elif("listen songs" in text):
    spam=True
elif("play games" in text):
    spam=True
else:
    spam=False

if(spam):
    print("This text is a spam")
else:
    print("This is not a text spam")