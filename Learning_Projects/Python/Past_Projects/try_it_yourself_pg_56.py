# Michael Randall
# 01/21/2023
# Try it yourself Exercises pg 56 for python crash course 4-1 through 4-2

# 4-1 create a list of fav pizzas then loop through the list and add a message to the list, also a message outside of the loop

fav_pizza = ['pep', 'pinapple', 'six chesse'] 
for pizza in fav_pizza:
	print (f"This pizza is awesome, {pizza}")
print ("This is the list of best pizzas hands down")

# 4-2 Create a list of animals that have similar charctrisics then use a loop to iterate through the list saying something about the animals the add a statement outside of the loop saying what they have in common

animals = ["dog", "lama", "goat", "pig"]
for animal in animals:
	print (f"This is one of the best animals on the planet, {animal.title()}")
print ("Each of these have the cutest ears")
