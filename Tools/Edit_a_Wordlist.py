# Script to prepend hmr_ to kali wordlists

with open('Change_This_List_To_Edit.txt', 'r') as input_file:                     # Read chosen wordlist file
    wordlist = input_file.read().splitlines()                                     # Read each line in the file 

updated_wordlist = ['Change_This_What_to_Prepend' + word for word in wordlist]    # prepend to each word in the wordlist Change to the end if you want to append

with open('Change_This_New_List_Name.txt', 'w') as output_file:                   # create a new file need to change the name for each list
    output_file.write('\n'.join(updated_wordlist))                                # Write the updated wordlist to the new file 

print("Updated your word list with Change_This_to_What_is_Changed")    