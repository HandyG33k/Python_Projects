# 11/25/2024
# Caesar Encryption (also known as the Caesar Cipher) is a simple encryption technique that works by shifting the letters in the plaintext message by a certain number of positions.
#The challenge: Create a function that has two parameters – a string to be encoded and an integer representing the number of positions each letter should be shifted.

import string


dic_letters = {up_letters:chr(up_letters+64) for up_letters in range(1,27)}  # Creates a key pair dictionary for the alphabet in uppercase using ASCII code 64 being Capital A it will pull uppercase letters then uses for loop to assign the number vaule to the letter 


Encrypt = input('What words would you like to encrypt?: \n\n').upper()  # Requests a text to be Encrypted and makes it uppercase to match dictionary 
Shifts = int(input('How many shifts would you like your encryption to preform?: \n\n')) # requests the amount of shifts to be applied to the requested text

def ceaser(param1 , param2):  # function to shift the letters 
    Cypher_list = []  # Creates a new list to store the shifted text
    for character in param1: # for loop pulling each character from the requested text 
        if character.isalpha():  # Checks to make sure the character is an alphabetic character then adds it to a nested for loop to shift it 
            postion =ord(character) - 64 # Orders the character utilizing the ASCII code like in the dicionary  
            new_postion = (postion + param2 -1) % 26 + 1  # Then creates a new postion for the character by shifting the requested times Takes postion of the character adds the shift variable -1 then uses modulo 26 + 1 to loop back around if the requested shift is more than 26
            Cypher_list.append(dic_letters[new_postion]) # appends the new postion the the cypher list created at the begining of the loop
        else:
            Cypher_list.append(character) # ignores all non alphabetic characters 
    return ''.join(Cypher_list) # Removes seperators and converts the list to a string 

Encrypted = ceaser(Encrypt, Shifts) # Add the requests to the Function 

print('Here is your encrypted text.\n\n',Encrypted) # Prints out the cypher text








            


