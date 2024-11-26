# 11/24/2024
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9. The sum of these multiples is 23. Find the sum of all multiples of 3 or 5 below 1000. 

# Create List of numbers 
group = list(range(1000))

# Pull a list of multiples of 3
Multiples_of_3 = [j for j in group if j % 3 == 0]

# Pull a list of multiples of 5
Multiples_of_5 = [i for i in group if i % 5 == 0]

# Combine the lists
all_multiples = Multiples_of_5 + Multiples_of_3

# Remove duplicates 
true_list = list(set(all_multiples))

# Sum the combined list 
total = sum(true_list)
print(total)








