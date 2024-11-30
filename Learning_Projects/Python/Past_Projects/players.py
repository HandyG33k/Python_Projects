# Michael Randall
# 01/22/2023
# Slicing lists 

# Using a colon in a print statement in sqaure brackets allows for a list to be partilly ran through 

	# Creating a list of players to work with this form does not do start at zero counting 

players = ['john', 'brad', 'eli', 'jake', 'jack', 'jane', 'allison']

	# Then printing out a part of the list by specifing with a collon in the brackets

print (players[0 : 4])

	# This can be done with any subset of the list 

print (players[4 : 7])

	# By leaving out the first argument the list will start at 1 and end where specified 

print (players[:3])

	# this can also be done to the rear of the list adding the colon after the first argument 

print (players[4:])

	# and using the negitive indexing it can be used to count from the back of the list 

print (players[-3:])

	# adding a thrid argument tells python how many item to skip

print (players[1 : 7 : 2])

# Looping using a slice of a list 

	# Using a for loop we can use a subset of the list for something else 

print (f'Here are the first three players of the team:')
for player in players[0:3]:
	print (player.title())



