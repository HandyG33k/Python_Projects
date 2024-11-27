import random

computer_number = random.randint(1, 100)

player_choice = ''


def compare(computer_number, player_choice):
    while computer_number != player_choice:
        player_choice = int(input("\nCan you guess the whole number I am thinking of between 1 and 100. \n"))
        if computer_number > player_choice:
            print("Your choice is to low try again \n")
        elif computer_number < player_choice:
            print("Your choice is to high try again \n")
        elif computer_number == player_choice:
            return print("Great Job you Win!!!! \n")

compare(computer_number, player_choice)