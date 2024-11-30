# Michael Randall
# 01/21/2023
# Organizing Lists practice

# Sorting list permanently using .sort() method

	# Create a list of cars to be sorted alphabeticaly

cars = ['bmw', 'mazda', 'ford', 'audi', 'jaguar']
print (cars)
cars.sort()
print (cars)
cars.sort(reverse=True)
print (cars)

	# Temporarily sort lists using sorted function

cars_second = ['bmw', 'toyota', 'audi', 'ford', 'dodge']
print (f'Here is the original list form, {cars_second}')
print (f'Here is the sorted version {sorted(cars_second)}')
print (f'Here is the list put back after the use of the function, {cars_second}')

	# printing a list in reverse order using the .reverse() method Permanent

cars_third = ['bmw', 'toyota', 'dodge', 'ford', 'audi', 'jaguar']
print (cars_third)
cars_third.reverse()
print (cars_third)

# Find the length of a list using the len() function 
print (f'This is the length of the first cars list. {len(cars)} cars')
print (f'This is the length of the second car list. {len(cars_second)} cars')
print (f'This is the length of the third car list. {len (cars_third)} cars')
