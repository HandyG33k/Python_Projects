# Michael Randall
# 01/15/2023
# The Try it Yourself from page 25 of Python Crash Course 2-3 through 2-7

# 2-3 Personal Message create a variable with a name and print a message to that person

	# Variables created for the names

person_a = "raidyn randall"
person_b = "renzo randall"
person_c = "Michael Randall"

	# Printed results with new lines added 
		
print ("Hello", person_a, "\nWould You Like To Play a Game?")
print ("\nHello", person_b, "\nWould You Like To Play a Game?")
print ("\nHello", person_c, "\nWould You Like To Play a Game?\n")

# 2-4 use variables to change the casing of the names permently

	# using .title() to make proper naming caps into a new variable

person_a =(person_a.title())

	# Using .upper() to make the name is all caps into a new variable

person_b =(person_b.upper())

	# Using .lower() to make the name all lowercase into a new variable

person_c =(person_c.lower())

	# Printed results with new lines added

print (person_a,'\n')
print (person_b,'\n')
print (person_c,'\n')

# 2-5 Find a qoute from a famous person you admire and print it with qoutation marks included

print ('Wayne Gretzky coined the saying:\n"You miss 100 percent of the shots you never take"\n')

# 2-6 Repeat 2-5 but use variables 

	# creating variables for the name of famous person and thier message then printing the  results

famous_person = "Wayne Gretzky"
message ='"You miss 100 percent of the shots you never take"'
print (famous_person,'coined the saying:','\n',message,'\n')

# 2-7 Use tabbing and new lines and then strip them as part of a variable

	# creating a variable with a tab in front and a new line after and printing results

name = "\tJohn Smith\n"
print (name)

	# Using .rstrip() to remove the new line are the variable and printing results

print (name.rstrip())

	# Using .lstrip() to remove the tab at the begging of the variable and printing results

print (name.lstrip())

	# Renaming the variable to strip out both the tab at the begging and new line after and printing results

name = (name.strip())
print (name)

