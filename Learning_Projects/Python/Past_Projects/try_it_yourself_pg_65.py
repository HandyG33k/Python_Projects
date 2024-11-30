# Michael Randall
# 01/22/2023
# Try it yourself pg 65 of Python Crash Course Exercises 4-10 through 4-12

# 4-10 Using the prior programs add lines to the end that print the first threee items in the list, print a message that slices out the middle item, and a message that slices out the last three items

players = ['john', 'brad', 'eli', 'jake', 'jack', 'jane', 'allison', 'joan', 'mike']

print (players[0:3])
print (players[3:6])
print (players[6:9])

# 4-11 use the program on pizzas from try it yourself pg 56 to make a copy of the pizza list and call it friends_pizzas and add a new pizza to the orignal list and a new pizza to the friends pizza list and prove that there is now two seperate list using a for loop for each 

fav_pizza = ['pep', 'pinapple', 'six chesse'] 
for pizza in fav_pizza:
	print (f"This pizza is awesome, {pizza}")
print ("This is the list of best pizzas hands down")

friends_pizza = fav_pizza[:]
print (fav_pizza)
print (friends_pizza)
friends_pizza.append('ham')
fav_pizza.append('sausage')

for pizza in fav_pizza:
	print (f"I love these pizzas, {pizza}")
print ("These are the pizzas my friend's favorite pizzas")
for fpizza in friends_pizza:
	print (f"They love, {fpizza}")
print ('Thanks for listening')

# 4-12 Use the lists from the foods.py exercise and add for loops to print the foods out 

my_foods = ['pizza', 'eggs', 'cookies', 'chips']
for food in my_foods:
	print (f"I love these foods, {food}")
friends_food = my_foods[:]
friends_food.append('cheese')
for foods in friends_food:
	print (f"These are the foods my friend loves, {foods}")
print ('These combined are the best foods')

