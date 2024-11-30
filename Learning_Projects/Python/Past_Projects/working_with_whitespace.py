# Michael Randall
# 01/15/2023
# Using Whitespace in Programs Used mostly to provide user input sanatation

# how to remove whitespace form the right end to clear up the the program using rstrip() you can clear up whitespace from the left using lstrip() on the call it is requested on

# setting variables with extra whitespace on left and right 
favorite_language = "Python\n"
also_favorite_language = " Python"
not_my_favorite_language = "\nC#\n"

# Printing the variable with the right whitespace and then using .rstrip() to remove it
print (favorite_language)
print (favorite_language.rstrip())

# Printing the variable with left whitespace and then removing it with .lstrip()
print (also_favorite_language)
print (also_favorite_language.lstrip())

# To permanently remove the whitespace the variable need to be renamed 
favorite_language = favorite_language.rstrip()
also_favorite_language = also_favorite_language.lstrip()

# Print the new Variables with removed whitespace
print (favorite_language)
print (also_favorite_language)

# If there is whitespace on both sides it can be removed with .strip()
print (not_my_favorite_language)
print (not_my_favorite_language.rstrip())
print (not_my_favorite_language.lstrip())
print (not_my_favorite_language.strip())

