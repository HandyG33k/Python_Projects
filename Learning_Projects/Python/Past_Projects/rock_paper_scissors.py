# Michael Randall
# 01/24/2023
# Rock, Paper, Scissors Game

# Imported Libs

import random

# Variables for the players 

computer_input = random.choice(['rock', 'paper', 'scissors'])
human_input = input("Please choose rock, paper, or scissors to play\n")

# Variables for the messages

tie_message = "Game is a Tie"
win_message = "You won the Game great job!!!"
lose_message = "Sorry it looks like you lost this one play again"

# Game Logic (Need to work on building it into a Loop)

if computer_input == 'scissors' and human_input == 'scissors':
	print (f"{tie_message} 'Computer choose'\n {computer_input}")
elif computer_input == 'scissors' and human_input == 'rock':
	print (f"{win_message} 'Computer choose'\n {computer_input}")
elif computer_input == 'scissors' and human_input == 'paper':
	print (f"{lose_message} 'Computer choose'\n {computer_input}")

if  computer_input == 'rock' and human_input == 'rock':
	print (f"{tie_message} 'Computer choose'\n {computer_input}")
elif computer_input == 'rock' and human_input == 'scissors':
	print (f"{lose_message} 'Computer choose'\n {computer_input}")
elif computer_input == 'rock' and human_input == 'paper':
	print (f"{win_message} 'Computer choose'\n {computer_input}")

if computer_input == 'paper' and human_input == 'paper':
	print (f"{tie_message} 'Computer choose'\n {computer_input}")
elif computer_input == 'paper' and human_input == 'rock':
	print (f"{lose_message} 'Computer choose'\n {computer_input}")
elif computer_input == 'paper' and human_input == 'scissors':
	print (f"{win_message}, 'Computer choose'\n {computer_input}")