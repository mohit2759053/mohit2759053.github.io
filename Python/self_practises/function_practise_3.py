# 3. Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336

def multiplication(numbers):
	multi = 1
	for i in numbers:
		multi *= i
	return multi
print(multiplication((8,2,3,-1,7)) )