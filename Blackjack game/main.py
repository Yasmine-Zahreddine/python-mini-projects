import random
import os


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def deal_card():
    '''returns a random card from the deck'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack game!"
    elif user_score == 0:
        return "Win with a Blackjack game!"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"


def play_game():
    game_over = False
    clear_terminal()
    print(logo)
    user_cards = []
    computer_cards = []
    user_cards.append(deal_card())
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    computer_cards.append(deal_card())
    computer = calculate_score(computer_cards)
    user = 0
    while not game_over:
        user = calculate_score(user_cards)
        print(f"    Your cards: {user_cards}, current score : {user}")
        print(f"    Computer's first card: {computer_cards[0]}")
        if user == 0 or computer == 0 or user > 21:
            game_over = True
        else:
            cont = input("\nType 'y' to get another card, type 'n' to pass: \n")
            if cont == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True
    while computer != 0 and computer < 17:
        computer_cards.append(deal_card())
        computer = calculate_score(computer_cards)
    print(f"\n    Your final hand: {user_cards}, final score {user}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer} \n")
    print(compare(user, computer))


clear_terminal()
while input("Do you want to play a game of Blackjack game? Type 'y' or 'n' : ") == 'y':
    clear_terminal()
    play_game()
