# Michael Randall
# 01/21/2023
# Working with number lists

# using the range function and a for loop allows to print out numbers easliy remember that python use the off by one format

for value in range(1, 51):
	print (value)

# If you want to print zero to only add one argument still will have the off by one nature

for value in range(51):
	print (value)

# Next we can use the list() function to create a list of numbers as well

numbers = list(range(1, 11))
print (numbers)

# Adding a thrid argument to the range() function tells python how many number to skip as it builds a list of numbers 

even_numbers = list(range(2, 11, 2))
odd_numbers = list(range(1, 11, 2))
print (odd_numbers)
print (even_numbers)

# You can create allmost any list of number using range() try creating a list of the first 10 square roots into a list 

squares = []
for value in range(1, 11):
	square = value ** 2
	squares.append(square)

print (squares)

# print the binary number through 100

binaries = []
for value in range(2, 101, 2):
	binaries.append(value ** 2)

print (binaries) 

# Using min() to find the minimum amount of number in a listt and max() to find the maximum amount of numbers in a list and sum() to add the numbers in a list

digits = range(1, 101)
print (min(digits))
print (max(digits))
print (sum(digits))

# Using list comprehensions help minimize code by including the for loop into the list directly elemiating the need for the colon and indenting 

squares = [value**2 for value in range(1, 101)]
print (squares)

binaries = [value**2 for value in range(1, 101, 2)]
print (binaries)