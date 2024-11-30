# Michael Randall
# 01/15/2023
# Try it Yourself 3-1 through 3-3

# 3-1 Create a list of the names of friends called names and print each name one at a time

	# List of friends 
names = ['charles', 'paul', 'josh', 'jason', 'jayna', 'raul']

	# printing each name
print (names[0].title())
print (names[1].title())
print (names[2].title())
print (names[3].upper())
print (names[-2].title())
print (names[-1].upper())

# 3-2 Use the same list to create a message that is the same to each person but uses their name

message = 'I hope you have been well,'

print (message,names[0].title())
print (message,names[1].title())
print (message,names[2].title())
print (message,names[3].title())
print (message,names[4].title())
print (message,names[5].title())

# 3-3 Create a list of favorite transportaion models and print some statement about them

car_models = ['subaru sti', 'ford bronco', 'honda civic']
print ('I would love own a',car_models[0].title())
print ('I would love own a',car_models[1].title())
print ('I would love own a',car_models[2].title())

