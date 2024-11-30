# Michael Randall
# 01/15/2023
# Working with Numbers

# Using math operators on integers 

	# Adding
print ('2 + 3 is', 2 + 3) 

	# Subtracting

print ('3 - 2 is', 3 - 2)

	# Multipling

print ('2 * 3 is', 2 * 3)

	# Dividing

print ('3 / 2 is', 3 / 2)

	# Using Exponents with double **

print ('3 to the power of 2 is', 3 ** 2)
print ('3 to the power of 3 is', 3 ** 3)
print ('10 to the power of 6 is ', 10 ** 6)

	# Using the order of operations in math

print ('2 + 3 * 4 is', 2 + 3*4)
print ('(2 + 3) * 4 is', (2 + 3) * 4)

# Using math with Floats (a number with a decimal)

	# Using math operators with floats is the same as integers for the most part 

print ('0.1 + 0.1 is',0.1 + 0.1)
print ('0.2 + 0.2 is',0.2 + 0.2)
print ('2 * 0.1 is', 2 * 0.1)
print ('2 * 0.2 is',2 * 0.2)

	# Sometimes Python will provided arbitary zeros in a float Will learn later how to deal with them
print ('0.2 + 0.1 is',0.2 + 0.1)
print ('3 * 0.1 is',3 * 0.1)

# Dividing integers and combining integers and floats with math will always result in a float

print ('4 / 2 is',4/2)
print ('1 + 2.0 is',1 + 2.0)
print ('2 * 3.0 is',2 * 3.0)
print ('3.0 to the power of 2 is',3.0 ** 2)

# Using underscores to make larger number easier to read in code Using the underscores allows for the normal seperation like commas but will print out with out them

universe_age = 14_000_000_000
print ("The universe's age is",universe_age)

# Using commas you can assign multiple variables at the same time 

x, y, z = 0, 0, 0
print ('The x axis is',x)
print ('The y axis is',y)
print ('The z axis is',z)

# constants are repersented with all caps notation and should stay the same through out the program

MAX_CONNECTIONS = 5000
print ('What is the max possable connections?',MAX_CONNECTIONS)

