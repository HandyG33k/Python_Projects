# Michael Randall
# 01/15/2023
# Using variables in Strings to create a full name

# Setting variables for the name 

first_name = "ada"
last_name = "lovelace"

# create a new variable using a f-string to call both variables to create one string using curly brackets to call the variables
full_name =f"{first_name} {last_name}"

# call the full name to be printed using .title() and the call each variable indivually with the .title() method as well
print (full_name.title())
print (first_name.title())
print (last_name.title())

# Use and f-string to say hello to ada 
print (f"Hello {first_name.title()} {last_name.title()}!")
print ("How are you?")

# doing the same as above using less typing 
print(f"Hello {full_name.title()}!")
print ("How are You?")

# Even better is making the f-string into its own variable and use the \n to add the new line instead of creating a new message to print 
message = (f"\tHello {full_name.title()}!\n\tHow are You?")
print (message)