# Michael Randall 
# 01/22/2023
# Copying a lists

	# create a list of favorite foods and copy it to a friends list of favorite foods by using the [:] this creates a copy of the whole list that can be added to a variable and saved

my_foods = ['pizza', 'eggs', 'cookies', 'chips']
friends_foods = my_foods[:]

print (f'My favorite foods are: {my_foods}')
print (f"\nMy friend's favorite foods are: {friends_foods}")

	# add a new food to each new list to prove they are each their own list 

my_foods.append('cheese')
friends_foods.append('toast')

print (f"My new list of favorite foods is: {my_foods}")
print (f"My friends new list of favorite foods are: {friends_foods}")

	# What wont work is not using the copy [:] and setting the variable as my_foods = friends_foods this would update the friends food with my food with every change
my_foods = friends_foods
print (f"See now they just match insead of have a diffent piece each.\n{my_foods}\n{friends_foods}")

