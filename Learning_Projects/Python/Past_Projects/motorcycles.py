# Michael Randall
# 01/16/2023
# Adding, Changing, and removing items from a list

# Creating the itiaial Motorcycle list 

motorcycles = ['honda', 'yamaha', 'suzuki']
print ('This the initial list created', motorcycles)

# Changing the first element of the list to something else

motorcycles[0] = 'ducati'
print ('This is the list with Honda replaced by Ducati', motorcycles)

# Changing the first item back and appending the new item to the list using .append() method

motorcycles[0] = 'honda'
motorcycles.append('ducati')
print ('This is the list with Honda put back and Ducati added to the list', motorcycles)

# Using the .append() method lists can be bulid dynamicly

	# Changing the list of motorcycles to nothing

motorcycles = []
print ('This is the list cleared', motorcycles)

	# Using the .append() method to add the makes back to the list one at a time

motorcycles.append('honda')
print ('Here is the first element added back', motorcycles)
motorcycles.append('yamaha')
print ('Here is the second added back', motorcycles)
motorcycles.append('suzuki')
print ('Here is the third added', motorcycles)
motorcycles.append('ducati')
print ('Here is the final one added', motorcycles)

# Inserting item in to a list using the .insert() method

motorcycles.insert(0, 'harley')
print ('This is an example of using the .inset() method to add an item to the 0 postion of a list',motorcycles)

# This is how to use a del statement to delete an item from a known position

del motorcycles[0]
print ('Here I used a del statement to delete the 0 position of the list', motorcycles)

# This is how to use removed item later using the .pop() method creating a second list of poped items

motorcycles.insert(4, 'harley')
print ('Added Harley back to the list at the end', motorcycles)

	# Using the .pop() method I will move Harley to the .pop() list By creating a variable named poped_motorcycles and adding the value of mototrcycles.pop() it will take the last item of the motorcycle list and add it to the poped list 

poped_motorcycles = motorcycles.pop()
print ('Motorcyles list has poped Harley out of it', motorcycles)
print ('Poped list has the last item Harley in it now', poped_motorcycles)

	# If the list was crnological then I could rename the the poped list to last_owned and crate a format string to list my last owned motorcycle

last_owned = motorcycles.pop()
print (f'The last motorcycle I owned was {last_owned.title()}')

	# this created a problem as now I have two poped list to fix I will change the first to the second

last_owned = poped_motorcycles
print (f'This is the acutal last motorcycle I owned {last_owned.title()}')
print ('Did I mess up the motorcycles list?', motorcycles)
print ('Yes I did is the Ducati in last_owned too?', last_owned)
print ('No it is not is there also a poped_motorcycles list floating', poped_motorcycles)
motorcycles.append('ducati')
print ('Yup by putting the Ducati in the wrong poped list then renaming it I lost the Ducati now I added it back', motorcycles)

# Now I am going to pop item from the list from any postion

first_owned = motorcycles.pop(0)
print ('Now the first item is poped from the initial list', motorcycles)
print (f'And I can use a format string to show my first owned motorcycle a {first_owned.title()}, and my last owned motorcycle a {last_owned.title()}.')

# If there is a long list and you dont know the postion number it can be removed with a value as well using the .remove() method

motorcycles.remove('suzuki')
print ('Using the .remove() method I removed the Suzuki because I have never owned a Suzuki', motorcycles)

	# If we want we can make the reson known with a new variable for the removal

motorcycles.append('suzuki')
print ('Added Suzuki back to remove it to a more discriptive variable', motorcycles)
would_not_own = motorcycles.remove('suzuki')
print (f'Now I removed the Suzuki from {motorcycles}, and added it to the would not own list {would_not_own}.')
	# That did not work :( I did it in the wrong order I need to list the Suzuki as the would not own motorcycle then use the .remove() to add it Also remember .remove() will only remove the first instance of the variable if there is more than one instance in the listt a loop is required 

motorcycles.append('suzuki')
print ('Readded Suzuki to the motorcycle list', motorcycles)

would_not_own = 'suzuki'

motorcycles.remove(would_not_own)

print (f'I changed the variable would_not_own to {would_not_own.title()} and used motorcycles.remove(would_not_own) to remove the variable from {motorcycles}')
print (f'Now I have one list for motorcycles {motorcycles}, and three variables first is the last owned motorcycle a {last_owned.title()}, second is the first owned motorcycle a {first_owned.title()}, and third is would not own motorcycles a {would_not_own.title()}')










