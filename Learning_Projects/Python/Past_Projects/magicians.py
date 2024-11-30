# Michael Randall
# 01/21/2023
# Working with list using for loops

#  Using a for loop to print out an entire list 
	# Creating a list of magicians

magicians =['brian', 'alice', 'bob', 'david', 'carolina']

	# Creating a variable called magician that is 'in' a for loop

for magician in magicians:

	# Printing a message to each magician in the list of Magicians

	print (f"{magician.title()}, That was an amazing trick!!\n")

	# Using the loop to add more messages by maintaing the indentation

	print (f"\tI can't wait to see the next one {magician.title()}\n")

	# exiting the indentation will ceate a break in the loop

print ("Thank you, all that was so fun!!!")
