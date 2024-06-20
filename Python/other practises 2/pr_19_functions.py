#if the number of arguments is unknown, add * before the parameter name:
def my_function(*kids):
	print("The older child is "+ kids[3])

my_function("rohan","sohan","geeta","babita","harsh")
