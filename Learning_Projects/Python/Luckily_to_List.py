# 11/28/2024
#Luckily to numbers
#Create a function in Python that accepts two parameters. The first will be a numbers of numbers. The second parameter will be a string that can be one of the following values: asc, desc, and none.
#If the second parameter is “asc,” then the function should return a numbers with the numbers in ascending order. If it’s “desc,” then the numbers should be in descending order, and if it’s “none,” it should return the original numbers unaltered.
import random

# Generate and shuffle numbers
numbers = list(range(1, 50))
print(numbers)
#random.shuffle(numbers)

#def new_func():
#    for i in range(0, len(numbers)):
#        for j in range(i+1, len(numbers)):
#            if numbers[i] >= numbers[j]:
#                numbers[i], numbers[j] = numbers[j], numbers[i]
#print(numbers)              
#
#new_func()


#how = input('I have created a random numbers of numbers for you. How would you like me to order them?: \n Type asc to have them ordered in asending order: \n Type desc to have them in desending order: \n Or type none to have them in there random format: \n')
#
#def chose(numbers, how):
#    if how == asc():
#        print(numbers[x])
#
#chose(numbers, how)
#

