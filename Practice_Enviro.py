import json
import sys

people = {}
cars = {}

def addingStuff():
	item = raw_input("What do you want to add: person, car, or quit?\n")
	if (item.lower() == 'quit'):
		quit()
	elif (item.lower() == 'person'):
		name = raw_input("What name would you like to add?\n")
		age = raw_input("What is their age?\n")
		people[name] = age
		#with open('Test.json', 'w') as f: json.dump(stuff, f, indent = 2)
		toJson(people)
		print ('{} was added to list\n'.format(name))
	elif(item.lower() == 'car'):
		carname = raw_input("What do you want to name this car?\n")
		year = raw_input("What is the year of the vehicle?\n")
		make = raw_input("What is the make of the vehicle?\n")
		model = raw_input("What is the model of the vehicle?\n")
		cars[carname] = year, make, model
		toJson(cars)
		#with open('Test.json', 'w') as f: json.dump(cars, f, indent = 2)
		print ('{} was added to list\n'.format(carname))
	else:
		print('Please enter an accepted value')
		return



def toJson(writefile):
	with open('Test.json', 'a') as f: json.dump(writefile, f, indent = 2)

def quit():
	exit()

while True:
	addingStuff()