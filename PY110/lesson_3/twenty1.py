'''Twentyone card game. User plays against dealer computer.'''

import os
import random
import time

ROYALTY = ['Jack', 'King', 'Queen']
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'King', 'Queen', 'Ace']
ROYALTY_VALUE = 10
STARTING_CARDS = 2
MAXIMUM_HAND_SCORE = 21
MAX_DEALER_HIT = 17
STRING_VALUE = 3
VALID_STAY = ['stay', 's']
VALID_HIT = ['hit', 'h']

def display_prompt(message):
    '''display user prompts formatted'''
    print(f"==> {message}")


def display_error():
    ''' Output error message for invalid input '''
    print('\n!!! ERROR: Invalid input, try again. !!! \n')


def display_header(message):
    ''' Output formated header message '''
    print(f"* {message} *    \n")



def display_pause(message):
    '''display loading screen to make game more alive'''
    sleep_clear_terminal(.5)
    print(f"{message}")
    sleep_clear_terminal(.5)
    print(f"{message} .")
    sleep_clear_terminal(.5)
    print(f"{message} .    .")
    sleep_clear_terminal(.5)
    print(f"{message} .    .    .")
    sleep_clear_terminal(.5)


def display_intro():
    ''' Output welcome message, intro, and objective of game. '''
    os.system('clear')
    display_header('WELCOME TO TWENTYONE!')
    sleep_clear_terminal(1.3)
    display_header('RULES')
    display_prompt("The goal of Twenty-One is to try to get as close to 21\n"
           "    as possible without going over. If you go over 21,\n"
           "    it's a bust, and you lose.\n")
    display_prompt("You always go first, and can decide to either "
           "hit or stay.\n"
           "    A hit means you want to be dealt another card.\n"
           "    To stay means you want to keep your current hand.\n"
           "    The dealer must hit until their card total is at least 17.\n"
           "    If the dealer busts, then you win!\n")
    display_prompt("Card Values:\n"
           "    * 2 - 10 = face value\n"
           "    * Jack, Queen, King = 10\n"
           "    * Ace  = 1 or 11 (whichever allows you to be closest to 21)\n"
           )
    time.sleep(1)
    input("==> Press 'Enter' to continue.")
    os.system('clear')


def display_shuffle(deck):
    '''display cards being shuffled:
    deck displayed != shuffled deck in game'''
    for num in range(20):
        os.system('clear')
        shuffle_deck = shuffle(deck)
        print(f'SHUFFLING DECK: {shuffle_deck[num]}')
        time.sleep(.1)
    os.system('clear')


def display_new_card(player_cards):
    '''display result of players hit: 
    output what card was added to their hand'''
    display_prompt(f'{player_cards[-1]} was added to your cards')
    time.sleep(1)


def sleep_clear_terminal(seconds):
    '''pause terminal and then clear terminal display'''
    time.sleep(seconds)
    os.system("clear")


def shuffle(deck):
    '''shuffle and return deck of cards'''
    random.shuffle(deck)
    return deck


def get_starting_hands(deck):
    '''return dealer_cards and player_cards'''
    dealer_cards = [deck.pop() for _ in range(STARTING_CARDS)]
    player_cards = [deck.pop() for _ in range(STARTING_CARDS)]

    display_prompt(f'Dealer has: {dealer_cards[0]} and unknown card')
    display_prompt(f'You have: {player_cards[0]} and {player_cards[1]}')

    return dealer_cards, player_cards


def hit(deck, cards):
    '''hit: grab a card from deck, update cards of player who hit'''
    card = deck.pop()
    cards.append(card)

    return cards, deck


def format_cards(cards):
    ''' return list of cards as string 
    so when displaying it isn't wrapped in list brackets'''
    str_cards = [str(elem) for elem in cards]
    return ', '.join(str_cards)


def calculate_cards_no_ace(player_cards):
    '''loop through inventory of a players cards,
    calculate sum of roylaty cards and sum of value cards,
    return as sum_cards_no_ace, also returns ace count'''
    sum_card_no_string = []
    sum_royalty_cards = []
    count_ace = 0

    for card in player_cards:
        if card == 'Ace':
            count_ace += 1
            continue
        if card in ROYALTY:
            sum_royalty_cards.append(card)
        else:
            sum_card_no_string.append(card)

    sum_cards_no_ace = (
        (len(sum_royalty_cards) * ROYALTY_VALUE) + sum(sum_card_no_string)
        )

    return sum_cards_no_ace, count_ace


def determine_ace(sum_cards_no_ace, count_ace):
    '''return the best ace choice for current round:
        - if count of aces only 1: return 1 or 11, 
        - else return list of ace best choice (1 or 11) 
        for sum_cards_no_ace'''
    if count_ace == 0:
        return count_ace
    if count_ace < 2:
        ace = 11 if sum_cards_no_ace <= 10 else 1

    else:
        ace = [11 for _ in range(count_ace)]

        for num in range(count_ace):
            if is_bust(sum_with_aces(sum_cards_no_ace, ace)):
                ace[num] -= 10
    return ace


def sum_with_aces(sum_cards_no_ace, ace):
    '''return total sum of player cards: 
    proper aces + rest of cards'''
    if not isinstance(ace, list):
        return ace + sum_cards_no_ace
    return sum(ace) + sum_cards_no_ace


def is_bust(total_card_sum):
    '''return boolean of if sum of player cards is greater than 21:
        True -> aka bust
        False -> sum is under 21
    '''
    return total_card_sum > MAXIMUM_HAND_SCORE


def find_card_total(cards):
    '''return sum of a players cards'''
    sum_cards_no_ace, count_ace = calculate_cards_no_ace(cards)
    ace = determine_ace(sum_cards_no_ace, count_ace)
    total_card_sum = sum_with_aces(sum_cards_no_ace, ace)

    return total_card_sum


def cards_value_only(cards):
    '''return list of players cards by value only
    if string value (royalty) then leave as is
    else convert to int (face value card)'''
    value_cards = []

    for elem in cards:
        card_string = elem.split()
        value = card_string[0]
        if len(value) < STRING_VALUE:
        # if not a string value ('king', 'ace', ...)
            value = int(value)
        value_cards.append(value)
    return value_cards


def player_turn(total_card_sum):
    '''Player turn: 
    ask if hit or stay'''
    while True:
        answer = input('\n==> Hit or Stay? (h/s): ')
        if answer.casefold() in VALID_STAY or is_bust(total_card_sum):
            return 'stay', total_card_sum
        if answer.casefold() in VALID_HIT:
            return 'hit'
        display_error()


def player_hit(player_cards, player_sum):
    '''output results of players hit, 
    return result of if they want/can hit again or not'''
    display_new_card(player_cards)
    display_prompt( f'Sum of your cards: {player_sum}'
            f' | Cards: {format_cards(player_cards)} ')
    return player_turn(player_sum)


def dealer_turn(dealer_card_sum, cards, deck):
    '''dealer's turn:
    if their total_card_sum is less than 17 -> hit
    elif total_card_sum is >= 17 -> stay'''
    display_pause("DEALER'S TURN")
    while dealer_card_sum < MAX_DEALER_HIT:
        print('Dealer hit!')
        sleep_clear_terminal(1.1)
        cards, deck = hit(deck, cards)
        dealer_card_value = cards_value_only(cards)
        dealer_card_sum = find_card_total(dealer_card_value)
    print('Dealer chose to stay!')
    return dealer_card_sum, cards


def determine_winner(player_sum, dealer_sum):
    '''once both players stay, determine winner'''
    if player_sum > MAXIMUM_HAND_SCORE:
        return 'You busted! Dealer'
    if dealer_sum > MAXIMUM_HAND_SCORE:
        return 'Dealer busted! You'
    if player_sum == dealer_sum:
        return 'Tie!'
    winner = 'You' if player_sum > dealer_sum else 'Dealer'
    return winner


def game_results(winner, player_sum, dealer_sum, both_player_cards):
    '''display game results'''
    display_pause('GATHERING RESULTS')
    display_header('RESULTS')
    if winner == 'Tie!':
        display_prompt(f'{winner}')
    else:
        display_prompt(f'{winner} won!')
    display_prompt(f"Your score: {player_sum} |"
                   f" Your cards: {format_cards(both_player_cards[0])}")
    display_prompt(f"Dealer score: {dealer_sum} |"
                   f" Dealer cards: {format_cards(both_player_cards[1])}\n")
    display_header('GAME OVER')


def play_again():
    ''' Ask player if they would like to play again:
        - y -> new match
        - n -> terminate game 
        - else error message
    '''
    answer = input('\n==> Want to play again? (y/n): ')
    valid_answers = ['y', 'n', 'yes', 'no']

    while answer.casefold() not in valid_answers:
        display_prompt('ERROR: Invalid input, try again!')
        answer = input('\n==> Want to play again? (y/n): ')

    if answer[0].casefold() == 'y':
        os.system("clear")
        play_21()
    else:
        display_pause('See you later!')

def play_21():
    '''main entry point to play 21'''
    player_lost = None

    # SET UP GAME
    deck = [f'{value} of {suit}' for suit in SUITS for value in VALUES]
    display_shuffle(deck)

    shuffled_deck = shuffle(deck)
    dealer_cards, player_cards = get_starting_hands(shuffled_deck)
    dealer_card_value = cards_value_only(dealer_cards)
    player_card_value = cards_value_only(player_cards)
    player_sum = find_card_total(player_card_value)
    display_prompt(f'Your card sum: {player_sum}')

    # PLAYER TURN
    hit_or_stay = player_turn(player_sum)

    while hit_or_stay == 'hit':
        player_cards, shuffled_deck = hit(shuffled_deck, player_cards)
        player_card_value = cards_value_only(player_cards)
        player_sum = find_card_total(player_card_value)

        if is_bust(player_sum):
            player_lost = True
            display_new_card(player_cards)
            break

        hit_or_stay = player_hit(player_cards, player_sum)

    # DEALER TURN
    dealer_sum = find_card_total(dealer_card_value)
    if not player_lost:
        dealer_sum, dealer_cards = dealer_turn(
            dealer_sum, dealer_cards, shuffled_deck)
        dealer_card_value = cards_value_only(dealer_cards)

    # DETERMINE WINNER AND DISPLAY END GAME
    winner = determine_winner(player_sum, dealer_sum)
    game_results(winner, player_sum, dealer_sum, [player_cards, dealer_cards])
    play_again()

# INVOKE START OF GAME
display_intro() # only at start of 1st game display rules
play_21() # start game
