marks = int(input("Enter Your marks for know the grades\n"))

if(marks > 90):
	grade ="A+"
elif(marks>=80):
	grade = "A"
elif(marks>=70):
	grade = "B"
elif(marks>=60):
	grade = "C"
elif(marks>=50):
	grade = "D"
elif(marks>=40):
	grade = "E"
else:
	grade = "Failed" 	

print("Your grade is " + grade)	