import os
import random
from data import words

logo = r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __| |                      
                   |____|    '''

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def choose_mode():
    print("Welcome to Hangman!")
    print("Choose your game mode:")
    print("1. One Player (You guess the word)")
    print("2. Two Players (One player sets the word, the other guesses)")
    mode = int(input("Enter 1 or 2: "))
    while mode != 1 and mode != 2:
        mode = int(input("\nPlease make sure to enter 1 or 2: "))
    return mode


def one_player():
    print("You chose one player mode")
    chosen_word = random.choice(words)
    return chosen_word


def two_player():
    print("You chose 2 player mode")
    chosen_word = input("Please enter a word for the other player to guess\n")
    clear_terminal()
    print(logo)
    print("player 2 here comes your turn")
    return chosen_word


def play_game():
    print(logo)
    lives = 6
    mode = choose_mode()
    chosen_word = None
    if mode == 1:
        chosen_word = one_player()
    elif mode == 2:
        chosen_word = two_player()
    i = len(chosen_word)
    display = []
    while i > 0:
        display.append("_")
        i -= 1
    end_of_game = False
    entered_letters = []
    print(f"{' '.join(display)}")
    while not end_of_game:
        c = input("guess a letter: ").lower()
        flag = 0
        for i in range(len(chosen_word)):
            if c == chosen_word[i]:
                display[i] = c
                flag = 1
        if c == "\n":
            continue
        if c in entered_letters:
            print("You already entered this letter\n")
            continue
        elif flag == 0:
            lives -= 1
        print(f"{' '.join(display)}")
        print(stages[lives])
        entered_letters.append(c)
        if lives == 0 and (not end_of_game):
            end_of_game = True
            print("\n\nYou lost all your lives")
            print(f"the word was {chosen_word}")
        if "_" not in display:
            end_of_game = True
            print("You Won!!")


clear_terminal()
play_game()
while input("Want to play again? enter 'y' or 'n':  ") == 'y':
    clear_terminal()
    play_game()


clear_terminal()
