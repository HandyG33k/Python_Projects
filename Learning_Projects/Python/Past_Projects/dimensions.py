# Michael Randall
# 01/22/2023
# Truples and immutable list using () instead of []

# creating a truple and printing the indexes within 
dimensions = (200, 50)
print (dimensions[0])
print (dimensions[1])

# the truple is really just defined by the , and the () make it easier to read 

mt_t = 3,
print (mt_t)
	# this works too 

# using loops in truple is the same as lists 

dimensions = (200,50)
for dimension in dimensions:
	print (dimension)

# While truples are immuteable the variable they are assigned to can change 

dimensions = (200, 50)
print ('\nThese are the original dimensions')
for dimension in dimensions:
	print (dimension)

dimensions = (400, 100)
print('\nThis is the new dimensions')
for dimension in dimensions:
	print (dimension)

