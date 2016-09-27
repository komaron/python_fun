import basic_dict as bc
from hello_admin import *
from user_input import multiple
# A note about importing

# In python to import a full module at the top of your fle you type
# 'import module_name', this will import all the methods of the module.
# to use the module you would then called 'module_name.method_name()'
# Another alternative is to import function(s) you need rather than the whole
# repo. Ex 'from module_name import function1, function2, function3'. You can
# also import a module and give it another name Ex. 'import module_name as mn'
# then you can do 'mp.function_name'. To import a module and all its methods
# you can also 'from module_name import *' so you can then call all them methods
# with out specifying the module but this is bad when dealing with larger libraries

# Message
def display_message():
	'''Prints a very basic message about Python'''
	print('Let\'s learn about Python!')

def favorite_book(title):
	'''Print Favorite Book'''
	print('My favorite book is: ' + title)

def make_shirt(size,text='No text'):
	'''Creating a shirt given a size and text'''
	print("Shirt size: " + size + ", Text: " + text)

def make_album(artist, title):
	return {'artist': artist.title(), 'title': title.title()}

def show(list):
	for item in list:
		print(item)

def make_great(list):
	for item in list:
		list.insert(0,item + ' the Great')
		list.remove(item)

# Demonstration of using arbitrary parameters
def sandwich(*toppings):
	for i in toppings:
		print(i)
	print('Sandwich complete\n')

def build_profile(first,last,**info):
	profile = {}
	profile['first'] = first
	profile['last'] = last
	for key,value in info.items():
		profile[key]=value

	return profile

def main():
	# display_message()
	# favorite_book('Learning Python')
	# make_shirt('small', 'This shirt is awesome')
	# make_shirt(size = 'Large', text = "Dude")
	# make_shirt('small')
	# album = make_album('jim','Jim and the boys')
	# magician = ['Barney', 'Scooby Doo','Ernie']
	# show(magician)
	# make_great(magician)
	# show(magician)
	# print("Album: "+ album['title']+ ' by ' + album['artist'])
	#sandwich('bread', 'cheese', 'tomatoes', 'chicken')
	#sandwich('bread','cheese')
	kom = build_profile('Komaron', 'James', color='yellow',location='PA')
	print(kom)
main()
