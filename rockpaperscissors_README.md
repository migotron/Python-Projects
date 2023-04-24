Rock, Paper, Scissors Game
This is a simple Python implementation of the classic game "Rock, Paper, Scissors". The program generates a random choice for the computer and prompts the user to enter their choice. The user can choose from the options "R" for rock, "P" for paper, or "S" for scissors. The program then compares the user's choice with the computer's choice and determines the winner.

How to Play
    1.) Clone or download the repository to your local machine.
    2.) Open the file rps_game.py in a Python IDE or terminal.
    3.) Run the file to start the game.
    4.) The program will prompt you to enter your choice by typing "R", "P", or "S".
    5.) The program will generate a random choice for the computer.
    6.) The program will display the result of the game, indicating whether the user won, lost, or tied.

Function Definitions
    getUserChoice(): This function gets the user's choice and ensures that it is a valid choice of "R", "P", or "S".
    checkWhoWon(computer_choice, user_choice): This function determines the winner of the game by comparing the computer's choice with the user's choice.
    play_game(): This function calls the other two functions to start the game.