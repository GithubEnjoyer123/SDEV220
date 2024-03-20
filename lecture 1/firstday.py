print("Hello\n")

'''sets a test array full of values. Printing the -1 value will print the reverse order of the array, printing a 3'''
testArray = (0,1,2,3)
print(testArray[-1])

'''sets these variables to values of testArray'''
w,x,y,z = testArray

a = x + y
print(a)

'''Creates a set'''
my_set = {1,2,3,4}

'''Adds a value to set (in this case a is 3, so 3 + 3 = 6)'''
my_set.add(a+a)
print(my_set)

'''Returns true if value is in my set, else return false'''
print(3 in my_set)

'''Creates a dictionary, first the name and then its value'''
my_dict = {"name":"Evan","age":30}

'''Returns the value of name'''
print(my_dict["name"])