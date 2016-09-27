# Rental Car program
car = input('Favorite car brand? ')
print("Let's see if we can find you a " + car + " rental car.")

# Resturant Seating
group = input('How many people in your group? ')
group = int(group)
if group > 8:
	print('Parties greater than 8 must wait for a table.')
else:
	print('Table ready.')

# Muliples of 10
def multiple():
	num = input('Enter a number or a multiple of 10: ')
	num = int(num)
	if (num % 10) == 0:
		print('Value')
	else:
		print('Invalid')
		multiple()

multiple()


# Example of an annoying python program that will continue to mimic the
# users input until he or she enters a trigger word.
value = True
while value:
	message = input('What\'s the magic word? ')
	if message.lower() == 'walmart':
		value = False

	print(message)

