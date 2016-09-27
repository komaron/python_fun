# Reading the entire contents of a file and printing
with open('test.txt') as file_object:
	contents = file_object.read()
	print(contents)

# Making a list of lines from a file
with open('test.txt') as file_object:
	lines = file_object.readlines()
	for line in lines:
		print(line.rstrip())

# Writing to a text file
# Running this method will overwrite your file use append instead
# with open('test.txt','w') as file_object:
# 	file_object.write('This is a test')
with open('test.txt' 'a') as file_object:
	file_object.write('This is a test')
	name = input('What is your name?: ')

# Reading a file line by line and printing
# File has modes [read (r), write(w), append (a) and readWrite (r+)]
with open('test.txt') as file_object:
	for line in file_object:
		print(line.rstrip())
