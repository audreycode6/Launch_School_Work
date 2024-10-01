# # TODO: update main entry func to be concise, use helper functions

# import os
# import pdb
# import random
# import time

# ROYALTY = ['Jack', 'King', 'Queen']
# ROYALTY_VALUE = 10
# SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
# VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'King', 'Queen', 'Ace']
# STARTING_CARDS = 2
# AVAILABLE_CARD_INDEX = 4

# def prompt(message):
#     print(f"==> {message}")


# def display_header(message):
#     ''' Output formated header message '''
#     print(f"* {message} *    \n")

# '''test card deck data type:'''

# # dict: key -> string of card 'value of suit': value -> value of card
# # dict_deck = {f'{value} of {suit}':value for suit in SUITS for value in VALUES}
# # # print(dict_deck)
 
# # OR list: deck of cards with formated names: value of suits
# formatted_deck = [f'{value} of {suit}' for suit in SUITS for value in VALUES]

# # # OR list: deck of card values (no suits)
# # deck = [value for suit in SUITS for value in VALUES]


# # # OR list: multiply values by 4 to get a deck of card values (no suits)
# # value_repeat = VALUES * 4
# # # print(deck)

# def display_card_value():
#     '''display card values '''
#     prompt("Card Values:\n"
#            "    * 2 - 10 = face value\n"
#            "    * Jack, Queen, King = 10\n"
#            "    * Ace  = 1 or 11 (whichever allows you to be closest to 21)\n"
#            )

# def intro_prompt():
#     ''' Output welcome message, intro, and objective of game. '''
#     print()
#     display_header('WELCOME TO TWENTYONE!')
#     time.sleep(1.3)
#     os.system('clear')
#     display_header('RULES')
#     prompt("The goal of Twenty-One is to try to get as close to 21\n"
#            "    as possible without going over. If you go over 21,\n"
#            "    it's a bust, and you lose.\n")
#     prompt("You always goes first, and can decide to either hit or stay.\n"
#            "    A hit means you want to be dealt another card.\n"
#            "    The dealer must hit until their card total is at least 17.\n"
#            "    If the dealer busts, then you win.\n")
#     display_card_value()
#     time.sleep(1)
#     input("==> Press 'Enter' to continue.")

# def display_shuffle(deck):

#     for num in range(20):
#         os.system('clear')
#         shuffle_deck = shuffle(deck)
#         print(f'SHUFFLING DECK: {shuffle_deck[num]}')
#         time.sleep(.1)
#     os.system('clear')

# def shuffle(deck):
#     '''shuffle  and return deck of cards'''
#     random.shuffle(deck)
#     return deck

# def deal_cards(deck):
#     ''' dealer_cards = [d_card1, d_card2]
#         - only display card1 when displaying: f'Dealer has: {card1} and unknown card'
#         player_cards = [p_card1, p_card2]
#         - display both: f'You have: {p_card1} and {p_card2}
#     '''
#     dealer_cards = deck[:2]
#     player_cards = deck[2:4]


#     return dealer_cards, player_cards

# def format_cards(cards):
#     str_cards = [str(elem) for elem in cards]
#     return ', '.join(str_cards)


# ''' test calculating aces:'''
# def calculate_cards_no_ace(player_cards):
#     '''loop through inventory of play_cards, calculate sum of roylaty cards and sum of value cards,
#     return as sum_cards_no_ace, also returns ace count'''
#     sum_card_no_string = []
#     sum_royalty_cards = []
#     count_ace = 0

#     for card in player_cards:
#         if card == 'Ace':
#             count_ace += 1
#             continue
#         elif card in ROYALTY:
#             sum_royalty_cards.append(card)
#         else:
#             sum_card_no_string.append(card)

#     sum_cards_no_ace = (
#         (len(sum_royalty_cards) * ROYALTY_VALUE) + sum(sum_card_no_string)
#         )
    
#     return sum_cards_no_ace, count_ace
 

# def determine_ace(sum_cards_no_ace, count_ace):
#     '''return the best ace choice for current round,
#     if count of aces only 1: return 1 or 11, 
#     else return list of ace best choices for sum_cards_no_ace'''
#     if count_ace == 0:
#         return 0
#     if count_ace < 2:
#         ace = 11 if sum_cards_no_ace <= 10 else 1
#     else:
#         '''
#         work with up to 4 aces
#         for each ace card assign as 11 value by default:
#         if sum of all cards > 21:
#             decrease ace value to 1 until all aces 1 
#             or until sum <= 21
#         '''
#         ace = [11 for _ in range(count_ace)]

#         for num in range(count_ace):
#             if is_bust(sum_all_cards(sum_cards_no_ace, ace)):
#                 ace[num] -= 10
#     return ace
        
# def sleep_clear_display(seconds):
#     time.sleep(seconds)
#     os.system("clear")

# def pause(message):
#     sleep_clear_display(.5)
#     print(f"{message}")
#     sleep_clear_display(.5)
#     print(f"{message} .")
#     sleep_clear_display(.5)
#     print(f"{message} .    .")
#     sleep_clear_display(.5)
#     print(f"{message} .    .    .")
#     sleep_clear_display(.5)


# def sum_all_cards(sum_cards_no_ace, ace):
#     '''return total sum of player cards: 
#     proper aces + rest of cards'''
#     if type(ace) is not list:
#         return ace + sum_cards_no_ace
#     return sum(ace) + sum_cards_no_ace

# def is_bust(total_card_sum):
#     '''return boolean of if sum of player cards is greater than 21:
#         True -> aka bust
#         False -> sum is under 21
#     '''
#     return total_card_sum > 21

# def find_card_total(cards):
#     '''return sum of a players cards'''
#     sum_cards_no_ace, count_ace = calculate_cards_no_ace(cards)
#     ace = (determine_ace(sum_cards_no_ace, count_ace))
#     total_card_sum = sum_all_cards(sum_cards_no_ace, ace)

#     return total_card_sum



# def hit(deck, cards):
#     '''hit: grab a card from deck, update cards of player who hit'''
#     available_card = deck[AVAILABLE_CARD_INDEX]
#     cards.append(available_card)
#     deck.pop(AVAILABLE_CARD_INDEX)

#     return cards, deck


# def player_turn(total_card_sum, cards, deck):
#     '''Player turn: 
#     ask if hit or stay'''
#     while True:
#         # TODO optional: make it more flexible to input 'stay'
#         answer = input('\n==> Hit or Stay?: ') 
#         if answer.casefold() == 'stay' or is_bust(total_card_sum):
#             return 'stay', total_card_sum
#         if answer.casefold() == 'hit':
#             return 'hit' # True
#         else:
#             error_prompt()


# def dealer_turn(dealer_card_sum, cards, deck):
#     '''dealers turn:
#     if their total_card_sum is less than 17 -> hit
#     elif  total_card_sum is >= 17 -> stay'''
#     # TODO only dealer turn when player stays
#     pause("DEALER'S TURN")
#     while dealer_card_sum < 17:
#         cards, deck = hit(deck, cards)
#         dealer_card_value = cards_value_only(cards)
#         dealer_card_sum = find_card_total(dealer_card_value)
#     return dealer_card_sum, cards


# def determine_winner(player_sum, dealer_sum):
#     '''once both players stay, determine winner'''
#     if player_sum > 21:
#         return 'Dealer'
#     elif dealer_sum > 21:
#         return 'Player'
#     elif player_sum == dealer_sum: 
#         return 'Tie!'
#     else:
#         winner = 'Player' if player_sum > dealer_sum else 'Dealer'
#         return winner


# def display_results(determine_winner, player_sum, dealer_sum, both_player_cards):
#     '''display game results'''
#     pause('GATHERING RESULTS')
#     display_header('RESULTS')
#     if determine_winner == 'Tie!':
#         prompt(f'{determine_winner}')
#     else:
#         prompt(f'{determine_winner} won!')
#     prompt(f'Your score: {player_sum} | Your cards: {format_cards(both_player_cards[0])}')
#     prompt(f'Dealer score: {dealer_sum} | Dealer cards: {format_cards(both_player_cards[1])}\n')
#     display_header('GAME OVER')


# def play_again():
#     ''' Ask player if they would like to play again:
#         - y -> new match
#         - n -> terminate game 
#     '''
#     answer = input('\n==> Want to play again? (y/n): ')
#     valid_answers = ['y', 'n']
#     while answer[0].casefold() not in valid_answers:
#         prompt('ERROR: Invalid input, try again!')
        
#     if answer[0].casefold() == 'y':
#         os.system("clear")
#         play_21()
#     else:
#         pause('See you later!')
#         return

# def error_prompt():
#     ''' Output error message for invalid input '''
#     print('\n!!! ERROR: Invalid input, try again. !!! \n')


# def cards_value_only(cards):
#     '''return cards by value only'''
#     value_cards = []

#     for elem in cards:
#         card_string = elem.split()
#         value = card_string[0]
#         if len(value) < 3: # aka if not a string value ('king', 'ace', ...)
#             value = int(value)
#         value_cards.append(value)
#     return value_cards


# def play_21():
#     '''main entry point to play 21'''
#     player_lost = None 
#     intro_prompt()
#     display_shuffle(formatted_deck)

#      # shuffle deck
#     shuffled_deck = shuffle(formatted_deck)

#     # deal cards, not formated (long card name)
#     player_cards, dealer_cards = deal_cards(shuffled_deck)
#     prompt(f'Dealer has: {dealer_cards[0]} and unknown card')
#     prompt(f'You have: {player_cards[0]} and {player_cards[1]}')

#     # convert long card to value only
#     dealer_card_value = cards_value_only(dealer_cards)
#     player_card_value = cards_value_only(player_cards)

#     # Player turn
#     ''' make into a func so it takes player_cards or dealer_cards'''
#     player_sum = find_card_total(player_card_value)
#     prompt(f'Your card sum: {player_sum}')
#     result = player_turn(player_sum, player_card_value, shuffled_deck)
#     if 'stay' in result:
#         player_sum = find_card_total(player_card_value)

#     while result == 'hit':
#         player_cards, shuffled_deck = hit(shuffled_deck, player_cards)
#         player_card_value = cards_value_only(player_cards)
#         if is_bust(find_card_total(player_card_value)):
#             prompt(f'{player_cards[-1]} was added to your cards')
#             time.sleep(1)
#             player_lost = True
#             player_sum = find_card_total(player_card_value)
#             break
#         else:
#             prompt(f'{player_cards[-1]} was added to your cards')
#             prompt( f'Sum of your cards: {find_card_total(player_card_value)}'
#                     f' | Cards: {format_cards(player_cards)} ')
#             result = player_turn(player_sum, player_card_value, shuffled_deck)

#     # DEALER TURN
#     dealer_sum = find_card_total(dealer_card_value)
#     if not player_lost:
#         dealer_sum, dealer_cards = dealer_turn(dealer_sum, dealer_cards, shuffled_deck)
#         dealer_card_value = cards_value_only(dealer_cards)

#     # compare player and dealer cards, determine winner:
#     card_values = [player_card_value, dealer_card_value] 
#     both_player_cards = [player_cards, dealer_cards]
#     player_sum = find_card_total(card_values[0])
#     dealer_sum = find_card_total(card_values[1])
#     winner = determine_winner(player_sum, dealer_sum) 

#     #display winner:
#     display_results(winner, player_sum, dealer_sum, both_player_cards)
#     play_again()


# play_21() # start game

import random

SUITS = ('H', 'D', 'S', 'C')
VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

def prompt(message):
    print(f"=> {message}")

def initialize_deck():
    deck = [f"{value}{suit}" for value in VALUES for suit in SUITS]
    random.shuffle(deck)
    return deck

def total(cards):
    sum_val = 0

    for card in cards:
        value = card[:-1]

        if value == "A":
            sum_val += 11
        elif value in ['J', 'Q', 'K']:
            sum_val += 10
        else:
            sum_val += int(value)

    # Correct for Aces
    for card in cards:
        value = card[:-1]
        if sum_val <= 21:
            break
        if value == "A":
            sum_val -= 10

    return sum_val

def busted(cards):
    return total(cards) > 21

def detect_result(dealer_cards, player_cards):
    player_total = total(player_cards)
    dealer_total = total(dealer_cards)

    if player_total > 21:
        return 'PLAYER_BUSTED'
    elif dealer_total > 21:
        return 'DEALER_BUSTED'
    elif dealer_total < player_total:
        return 'PLAYER'
    elif dealer_total > player_total:
        return 'DEALER'
    else:
        return 'TIE'

def display_results(dealer_cards, player_cards):
    result = detect_result(dealer_cards, player_cards)

    match result:
        case 'PLAYER_BUSTED':
            prompt('You busted! Dealer wins!')
        case 'DEALER_BUSTED':
            prompt('Dealer busted! You win!')
        case 'PLAYER':
            prompt('You win!')
        case 'DEALER':
            prompt('Dealer wins!')
        case _:
            prompt("It's a tie!")


def play_again():
    print("-------------")
    answer = input('Do you want to play again? (y or n) ')
    return answer == 'y'

def pop_two_from_deck(deck):
    return [deck.pop(), deck.pop()]

def hand(cards):
    return ', '.join(cards)

while True:
    prompt('Welcome to Twenty-One!')

     # initial deal
    deck = initialize_deck()
    player_cards = pop_two_from_deck(deck)
    dealer_cards = pop_two_from_deck(deck)


    prompt(f"Dealer has {dealer_cards[0]} and ?")
    prompt(f"You have: {player_cards[0]} and {player_cards[1]}, for a total of {total(player_cards)}.")

    # player turn
    while True:
        player_choice = input("Would you like to (h)it or (s)tay? ")
        if player_choice not in ['h', 's']:
            prompt("Sorry, must enter 'h' or 's'.")
            continue

        if player_choice == 'h':
            player_cards.append(deck.pop())
            foo = hand(player_cards)
            prompt('You chose to hit!')
            prompt(f"Your cards are now: {foo}")
            prompt(f"Your total is now: {total(player_cards)}")

        if player_choice == 's' or busted(player_cards):
            break

    if busted(player_cards):
        display_results(dealer_cards, player_cards)
        if play_again():
            continue
    else:
        prompt(f"You stayed at {total(player_cards)}")

    # dealer turn
    prompt("Dealer's turn...")

    while total(dealer_cards) < 17:
        prompt("Dealer hits!")
        dealer_cards.append(deck.pop())
        prompt(f"Dealer's cards are now: {hand(dealer_cards)}")

    if busted(dealer_cards):
        prompt(f"Dealer total is now: {total(dealer_cards)}")
        display_results(dealer_cards, player_cards)
        if play_again():
            continue
    else:
        prompt(f"Dealer stays at {total(dealer_cards)}")

    # both player and dealer stays - compare cards!

    print('==============')
    prompt(f"Dealer has {hand(dealer_cards)}, for a total of: {total(dealer_cards)}")
    prompt(f"Player has {hand(player_cards)}, for a total of: {total(player_cards)}")
    print('==============')

    display_results(dealer_cards, player_cards)

    if not play_again():
        break