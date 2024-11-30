# Michael Randall
# 01/16/2023
# Try it yourself assignments 3-4 through 3-7 on page 42 of Python Crash Course

# 3-4 make a list of at least three people you would like to invite to dinner then print a personal message to them

guest_list = ['albert einstien', 'aristotle', 'barack obama', 'robert oppenheimer', 'sun tzu']
message = 'you are formally invited to a wonderful dinner with me, Michael Randall'
print (f'{guest_list[0].title()}, {message}.\n{guest_list[1].title()}, {message}.\n{guest_list[2].title()}, {message}.\n{guest_list[3].title()}, {message}.\n{guest_list[4].title()}, {message}.\n')

# 3-5 One person invited can not make it print a personal note about the missing attendee and add a new member then print new invatations

print (f'Unfortunally {guest_list[1].title()} will not be able to make it to the party')
del guest_list[1]
guest_list.insert(1, 'brad pitt')
print (f'In his place we will graced with {guest_list[1].title()}.')
print (f'{guest_list[0].title()}, {message}.\n{guest_list[1].title()}, {message}.\n{guest_list[2].title()}, {message}.\n{guest_list[3].title()}, {message}.\n{guest_list[4].title()}, {message}.\n')

# 3-6 We now have space for three more guests add a print statement that we found a bigger table and will be inviting three more people. Then use the .insert method to add the new guest in the begining and middle of the list then the .append method to add  the last guest to the end and re print invatations

print ('Great news I have procured a larger table and will have room to invite three more guests')
guest_list.insert(0, 'orsen wells')
guest_list.insert(3, 'henry ford')
guest_list.append('jack white')
print (f'I am now please to invite {guest_list[0].title()}, {guest_list[3].title()}, and {guest_list[7].title()} to our party')
print (f'{guest_list[0].title()}, {message}.\n{guest_list[1].title()}, {message}.\n{guest_list[2].title()}, {message}.\n{guest_list[3].title()}, {message}.\n{guest_list[4].title()}, {message}.\n{guest_list[5].title()}, {message}.\n{guest_list[6].title()}, {message}.\n{guest_list[7].title()}, {message}.\n')

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
