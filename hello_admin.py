current_users = ['kjames', 'admin', 'mcole', 'test']
new_users = ['test', 'nbrer', 'ndrew']


if current_users and new_users:
	for dude in new_users:
		if dude in current_users:
			print('Duplicate user: ' + dude)
			print('\n Try again\n')
		else:
			print('Username avaliable and added\n')
			current_users.append(dude)

	for user in current_users:
		if user == 'admin':
			print('Hello '+ user + ', would you like to see a system report?')
		else:
			print('Welcome back ' + user)
else:
	print('We need to find some users')

