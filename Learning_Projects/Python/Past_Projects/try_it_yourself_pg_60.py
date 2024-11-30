# Michael Randall
# 01/21/2023
# Try it yourself form pg 60 in python crash course 4-3 through 4-9

# 4-3 create a for loop to count to 20 

count = [value for value in range(1, 21)]
print (count)

# 4-4 make a list of number to one million then use a for loop to print them 

count_million = [value for value in range(1, 1_000_001)]
#print (count_million)

# 4-5 make the list of one million numbers then min, max and ,sum them
print (min(count_million))
print (max(count_million))
print (sum(count_million))

# 4-6 make a list of the odd numbers from 4-3 

count = [value for value in range(1, 21, 2)]
print (count)

# 4-7 make a list of multiple of 3 from 3 to 30 and print them 

thirds = [value for value in range(3, 31, 3)]
print (thirds)

# 4-8 make a list of the first 10 cubes and print them

cubes = [value**3 for value in range(1, 11)]
print (cubes)

# 4-9 same as above already done