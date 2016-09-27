rick = {
	'first': 	'Rick',
	'last':   'Jones',
	'city': 	'Philadelphia',
	'state': 	'PA',
	'age': '24'
}
komaron = {
	'first': 	'Komaron',
	'last': 	'James',
	'city': 	'Philadelphia',
	'state': 	'PA',
	'age': 		'24'
}
jake = {
	'first':	'Jake',
	'last': 	'StateFarm',
	'city': 	'Philadelphia',
	'state': 	'PA',
	'age': 		'35'
}
people = [rick, komaron,jake]

print('Printing everything I know about people.')
for p in people:
	location = p['city'] + ', ' + p['state']
	print(p['first'] + ' ' + p['last'])
	print(location)
	print(p['age'])
	print('')

rivers = {
	'nile':					'Egypt',
	'hudson':				'New York',
	'wissahickon':	'Philadelphia',
	'fairmount': 		'Philadelphia'
}
for river, location in rivers.items():
	print('River ' + river + ' is located in ' + location)

for river in rivers.keys():
	print("River: " + river)

for loc in set(rivers.values()):
	print(loc)

