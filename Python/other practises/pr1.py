List_of_students =["ram","shyam","sita","rohan","ramesh","manmohan"]
name= input("Enter Name for Check the status\n")

if(name in List_of_students):
    print("congratulations,You have Passed the exam")
else:
    print("Sorry, You are failed")