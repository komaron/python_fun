# Quick note on importing classes, to import a class you can do the following
# 'from file_name import Class'
class Resturant():
	'''Simple resturant class'''
	def __init__(self, resturant_name, cuisine_type):
		self.name = resturant_name
		self.types = cuisine_type
		self.number_served = 0

	def set_numbers_served(self, value):
		self.number_served = value

	def increment_number_served(self, value):
		self.number_served += value

	def describe_resturaunt(self):
		print(self.name)
		print(self.types)

	def open_resturaunt(self):
		print('The following resturant is now open: ' + self.name)


class IceCreamStand(Resturant):
	def __init__(self,resturant_name, cuisine_type):
		super().__init__(resturant_name, cuisine_type)
		self.flavors = ['Chocolate', 'Vanilla', 'Strawberry']

	def display_flavors(self):
		for flavor in self.flavors:
			print('Flavor: '+flavor)



class User():
	def __init__(self,first_name,last_name):
		self.first = first_name
		self.last = last_name
		self.logins = 0

	def increment_login_attempts(self):
		self.logins +=1

	def reset_login(self):
		self.logins = 0

	def describe_user(self):
		print('The users name is ' + self.first)
