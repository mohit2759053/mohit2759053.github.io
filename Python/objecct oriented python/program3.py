class Employee:
    pass

harry = Employee()

rohan = Employee()

harry.name = "harry"
harry.sallary = 123

print(harry.name,harry.sallary)

#it will throw error:
print(rohan.name,rohan.sallary)