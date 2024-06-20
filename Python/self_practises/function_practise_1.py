#2. Write a Python function to sum all the numbers in a list.
#Sample List : (8, 2, 3, 0, 7)
#Expected Output : 20



def sum(numbers):
	Total = 0
	for i in numbers:
		Total += i
	return Total
print(sum((8,2,0,3,7)))