# Michael Randall
# 01/21/2023
# Try it Yourself Page 46 from Python Crash Course 3-8 Through 3-10

# 3-8 seing the world make a list of five places you want to visit print the list as is, then use the function sorted() to print it more neatly Alphabetcly temporarily then reprint in origanl form then use the same function to reverse the list, and re print in original form, then permanently reverse the list using reverse() and print then change itt back using revese() and print, then permanetly sort the list in Alpha and print then use sort to reverse and print 

places_to_visit = ['italy', 'japan', 'england', 'spain', 'new york']
print (places_to_visit)
print (sorted(places_to_visit))
print (places_to_visit)
print (sorted(places_to_visit, reverse=True))
print (places_to_visit)
places_to_visit.reverse()
print (places_to_visit)
places_to_visit.reverse()
print (places_to_visit)
places_to_visit.sort()
print (places_to_visit)
places_to_visit.sort(reverse=True)
print (places_to_visit)


# 3-9 using the exercises from page 42 3-4 Through 3-7 and use len() to count the number of people invited 

	# 3-4 make a list of at least three people you would like to invite to dinner then print a personal message to them

guest_list = ['albert einstien', 'aristotle', 'barack obama', 'robert oppenheimer', 'sun tzu']
message = 'you are formally invited to a wonderful dinner with me, Michael Randall'
print (f'{guest_list[0].title()}, {message}.\n{guest_list[1].title()}, {message}.\n{guest_list[2].title()}, {message}.\n{guest_list[3].title()}, {message}.\n{guest_list[4].title()}, {message}.')
print (f'This is how many gests are invited {len(guest_list)}.\n')

	# 3-5 One person invited can not make it print a personal note about the missing attendee and add a new member then print new invatations

print (f'Unfortunally {guest_list[1].title()} will not be able to make it to the party')
del guest_list[1]
guest_list.insert(1, 'brad pitt')
print (f'In his place we will graced with {guest_list[1].title()}.')
print (f'{guest_list[0].title()}, {message}.\n{guest_list[1].title()}, {message}.\n{guest_list[2].title()}, {message}.\n{guest_list[3].title()}, {message}.\n{guest_list[4].title()}, {message}.')
print (f'This is how many gests are invited {len(guest_list)}.\n')

	# 3-6 We now have space for three more guests add a print statement that we found a bigger table and will be inviting three more people. Then use the .insert method to add the new guest in the begining and middle of the list then the .append method to add  the last guest to the end and re print invatations

print ('Great news I have procured a larger table and will have room to invite three more guests')
guest_list.insert(0, 'orsen wells')
guest_list.insert(3, 'henry ford')
guest_list.append('jack white')
print (f'I am now please to invite {guest_list[0].title()}, {guest_list[3].title()}, and {guest_list[7].title()} to our party')
print (f'{guest_list[0].title()}, {message}.\n{guest_list[1].title()}, {message}.\n{guest_list[2].title()}, {message}.\n{guest_list[3].title()}, {message}.\n{guest_list[4].title()}, {message}.\n{guest_list[5].title()}, {message}.\n{guest_list[6].title()}, {message}.\n{guest_list[7].title()}, {message}.')
print (f'This is how many gests are invited {len(guest_list)}.\n')

	# 3-7 It turns out you can only invite two guests use the .pop() method to remove one gueast at a time till all but two guests remain and print messages to the uninvited guests letting them know and print messages to the invited guests letting them know then use the del function to remove the last two and print the empty list

print ('Unfortunely it turns out I can only invite two guests.')
removed_message = ('Sorry I will have to remove your invite. I hope it is not has not put you out.')
invited_message = ('congrat you are one of the two guests invited')
print (f'{guest_list.pop().title()}, {removed_message}')
print (f'{guest_list.pop().title()}, {removed_message}')
print (f'{guest_list.pop().title()}, {removed_message}')
print (f'{guest_list.pop().title()}, {removed_message}')
print (f'{guest_list.pop().title()}, {removed_message}')
print (f'{guest_list.pop().title()}, {removed_message}')
print  (f'{guest_list[0].title()}, {invited_message}')
print  (f'{guest_list[1].title()}, {invited_message}')
del guest_list[1]
del guest_list[0]
print (guest_list)
print (f'This is how many gests are invited {len(guest_list)}.\n')

# 3-10 Make a list of your choice and use all of the functions from this chapter 

things_to_eat = ['beet', 'pizza', 'cracker', 'jam', 'apple', 'plum']
message = ('I ate a')

print (f'{message}, {things_to_eat[0].title()}')
print (f'Number of items I ate today {len(things_to_eat)}')
print (f'The things I ate today were, {things_to_eat}')
did_not_eat_yesterday = things_to_eat.pop()
print (f'Yesterday I did not eat a {did_not_eat_yesterday}')
print (f'The number of items I ate Yesterday were, {len(things_to_eat)}')
things_to_eat.append('plum')
print (f'Tomarrow I plan to eat {things_to_eat}. A total of {len(things_to_eat)} things')
print (f'If I put them in Alphabetacal order they would be {sorted(things_to_eat)}')
print (f'In reverse order would be {sorted(things_to_eat, reverse=True)}')
print (f'I think I would like the list to stay sorted in Alphabetacal order')
things_to_eat.sort() 
print (things_to_eat)
print ('Maybe I would like it in reverse now that I think of it')
things_to_eat.reverse()
print (things_to_eat)
print (f"I don't think I will ever eat {things_to_eat[1]} ever again")
things_to_eat.remove('pizza')
print (things_to_eat)
things_to_eat.insert(2, 'bean')
print (f"In it's place I will eat a, {things_to_eat[2]}")
print (things_to_eat)
print (f"Nevermind I don't like {things_to_eat[2]}, I am going to remove that")
del (things_to_eat[2])
print (things_to_eat)