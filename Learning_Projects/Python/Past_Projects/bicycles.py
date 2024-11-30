# Michael Randall
# 01/15/2023
# Lists Examples

# Using square brackets [] and commas you can create list that can be called later 

	# Using a list in this way will print the list and sqaure brackets ie ['trek', 'cannondale', 'redline', 'specialized']

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print (bicycles)

	# Using the index of the list will call the spcefic name in the list use square brackets to indicate the index within the list remember indexes start at 0

print (bicycles[0])
print (bicycles[1])
print (bicycles[2])
print (bicycles[3])

	# The same methods for casing is possable with lists 

print (bicycles[0].title())
print (bicycles[1].upper())
print (bicycles[2].lower())
print (bicycles[3].title())


	# Using a negitive index will pull from the end of the list starting with [-1] this is useful to pull from the end of the list without knowing the total length of the list

print (bicycles[-1])
print (bicycles[-2])
print (bicycles[-3])
print (bicycles[-4])

	# Using the index you can use indiviual parts of the list as vaiables combined with f-strings

message = f"My first bike was a {bicycles[0].title()}"
print (message)

