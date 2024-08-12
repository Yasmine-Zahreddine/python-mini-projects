import os
import random

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

logo = r"""
 _______                                _                                _                 
(_______)                           _  | |                              | |                
 _   ___ _   _ _____  ___  ___    _| |_| |__  _____    ____  _   _ ____ | |__  _____  ____ 
| | (_  | | | | ___ |/___)/___)  (_   _)  _ \| ___ |  |  _ \| | | |    \|  _ \| ___ |/ ___)
| |___) | |_| | ____|___ |___ |    | |_| | | | ____|  | | | | |_| | | | | |_) ) ____| |    
 \_____/|____/|_____|___/(___/      \__)_| |_|_____)  |_| |_|____/|_|_|_|____/|_____)_|    
                                                                                           
"""

def checkAnswer(target, guess):
    if target == guess:
        print("You got this righttt LESGGOOO")
        return True
    elif guess < target:
        print("Too low")
    else:
        print("Too high")
    return False

def setDifficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        return 10
    else:
        return 5

def playGame():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    tries = setDifficulty()
    target = random.randint(1, 100)
    game_over = False
    while not game_over:
        print(f"\nYou have {tries} attempts to guess the number\n")
        guess = int(input("Make a guess: "))
        if checkAnswer(target, guess):
            game_over = True
        else :
            tries -= 1
            if tries == 0:
                print("You lost\n")
                game_over = True


while input("Do you want to play the Number Guessing Game? Type 'y' or 'n' : ") == 'y':
    clear_terminal()
    playGame()
    
        
