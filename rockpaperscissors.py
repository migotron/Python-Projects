# Author: Miguel Ibarra【=◈︿◈=】
import random
import time

# Define the options available for the game
options = ["R", "P", "S"]

def getUserChoice():
    while True:                                                         # Create a loop that will continue until the user enters a valid choice
        user_choice = input("Enter your selection here (R, P, or S): ") # Get the user's choice
        user_choice = user_choice.upper() 
        if not user_choice:                                             # Check if the user didn't enter anything
            print("You did not enter anything! Try again.")
        elif user_choice not in options:                                # Check if the user's choice is not one of the options available
            print("Invalid selection! Make sure to enter a 'R', 'P', or 'S'! Try again.")
        else:                                                           # If the user entered a valid choice, exit the loop
            break
    return user_choice

def checkWhoWon(computer_choice, user_choice):
    if user_choice == computer_choice:                                      # Check if the user and computer have the same choice
        print("It's a tie! Both players chose " + user_choice)
    elif (user_choice == "P" and computer_choice == "R") or (user_choice == "R" and computer_choice == "S") or (user_choice == "S" and computer_choice == "P"):
        print("You win! " + user_choice + " beats " + computer_choice)      # If user chose the computer's choice weakness, i.e. Rock beats scissors, Paper covers rock, etc.
    else:
        print("You lose! " + computer_choice + " beats " + user_choice)     # If user did not choose the computer's choice weakness

def play_game():
    print("Rock, Paper, Scissors!") # Print a message to start the game
    time.sleep(1)                   # Wait for 1 second
    print("Rock, Paper, Scissors!") # Print the message again
    time.sleep(1)                   # Wait for another second
    print("Rock, Paper, Scissors!") # Print the message again


    # Get the computer's choice by randomly selecting an option from the list
    computer_choice = random.choice(options)
    # Get user's choice by calling the function
    user_choice = getUserChoice()
    # Check who won the game
    checkWhoWon(computer_choice, user_choice)

# Call the play_game function to start the game
play_game()