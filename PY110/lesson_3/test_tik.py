''' MY WAY: - diff: computer_protect/ computer_choose_square ... redundant code
Tiktactoe game: User plays on terminal with computer.
Computer plays offensively and defensively. 
Player to get score == MATCH_WON wins match.'''

import os
import random
import time

FIRST_PLAYER = 'Choose' # or 'Player' or 'Computer'
INITIAL_MARKER = " "
HUMAN_MARKER = "X"
COMPUTER_MARKER = "O"
MATCH_WON = 3
WINNING_LINES = [
    [1, 2, 3], # horizontal
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7], # vertical
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9], # diagonal
    [3, 5, 7],
]


def prompt(message):
    ''' Output formatted prompts for player '''
    print(f"==> {message}")


def display_header(message):
    ''' Output formated header message '''
    print(f"    * {message} *    ")


def error_prompt():
    ''' Output error message for invalid input '''
    print('\n!!! ERROR: Invalid input, try again. !!! \n')


def intro_prompt():
    ''' Output welcome message, intro and objective of game. '''
    print()
    display_header("Welcome to Tik Tac Toe.")
    print()
    prompt('Get 3 of your marks in a line (vertically, horizontally, or diagonally).')
    prompt(f"First player to reach {MATCH_WON} wins, wins the match!")
    prompt("Press Enter to start.")
    input()


def initialize_board():
    """ Return empty dictionary for positions of 3x3 board """
    return {square: INITIAL_MARKER for square in range(1, 10)}


def display_board(board, match):
    """ Output board to display in game: formatted and interpolated
    with dictionary awaiting user input """
    os.system("clear")

    prompt(f"You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.")
    display_header(f"Round {match}")
    print("")
    print("     |     |")
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
    print("     |     |")
    print("-----+-----+-----")
    print("     |     |")
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
    print("     |     |")
    print("-----+-----+-----")
    print("     |     |")
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print("     |     |")
    print("")



def empty_squares(board):
    """ Return list of available squares (aka INITIAL_MARKER) on board """
    return [key for key, value in board.items() if value == INITIAL_MARKER]


def string_available_squares(valid_choices, delimiter=", ", ending="or"):
    """ Return string of open squares on board that players may choose;
    format is different depending on # of open squares """
    length = len(valid_choices)

    if length < 1:
        formatted_choices = ""
    elif length == 1:
        formatted_choices = valid_choices[0]
    elif length == 2:
        formatted_choices = f"{valid_choices[0]} {ending} {valid_choices[1]}"
    else:
        formatted_choices = delimiter.join(valid_choices)
        formatted_choices = f"{formatted_choices[:-1]}{ending} {formatted_choices[-1]}"

    return formatted_choices


def choose_first_player(current_player):
    ''' Return the users choice for who will be the first player to start match
    ('Computer' or 'Player') '''
    while True:
        prompt('Choose which player goes first. Enter C for computer or P for yourself.')
        choice = input('c or p: ').casefold()
        if choice == 'p':
            current_player = 'Player'
            return current_player
        if choice == 'c':
            current_player = 'Computer'
            return current_player
        error_prompt()


def player_choose_square(board):
    ''' Update board with players square choice for players turn. '''
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f"Choose a square: {string_available_squares(valid_choices)}")
        square = input().strip()
        if square in valid_choices:
            break

        error_prompt()

    board[int(square)] = HUMAN_MARKER


def comp_offense(board):
    ''' Return square for computer to chose for turn if immediate threat exists for computer,
    (i.e player has 2 squares and board has open spot for 3rd winning spot for player);
    else False '''
    target_elem = None

    for line in WINNING_LINES:
        count_comp = 0
        count_intitial = 0
        for elem in line:
            if board[elem] == COMPUTER_MARKER:
                count_comp += 1
            if board[elem] == INITIAL_MARKER: # empty space
                count_intitial += 1
                target_elem = elem

            if (count_comp == 2 and count_intitial == 1): # chance for offense
                return target_elem
    return False  # no immediate threat


def comp_defend(board):
    ''' Return square for computer to choose if chance for winning, else False:
    (i.e computer has 2 squares and last square to win is empty) '''
    target_elem = None
    for line in WINNING_LINES:
        count_player = 0
        count_intitial = 0
        for elem in line:
            if board[elem] == HUMAN_MARKER:
                count_player += 1
            if board[elem] == INITIAL_MARKER: # empty square
                count_intitial += 1
                target_elem = elem

            if (count_player == 2 and count_intitial == 1): # chance to defend
                return target_elem

    return False  # no immediate threat


def computer_chooses_square(board):
    ''' Update board with computers choice:
    options in order of priority: offense move, defense moove, square 5, or random '''
    if board_full(board):
        return

    if comp_offense(board):
        square = comp_offense(board)
    elif comp_defend(board):
        square = comp_defend(board)
    else:
        if board[5] == INITIAL_MARKER:
            square = 5
        else:
            square = random.choice(empty_squares(board))

    board[square] = COMPUTER_MARKER


def board_full(board):
    ''' Return bool if board has empty squares or not '''
    return len(empty_squares(board)) == 0


def detect_winner(board):
    """ Return string of winner or falsy None value if tie """
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        if (
            board[sq1] == HUMAN_MARKER
            and board[sq2] == HUMAN_MARKER
            and board[sq3] == HUMAN_MARKER
        ):
            return "Player"
        if (
            board[sq1] == COMPUTER_MARKER
            and board[sq2] == COMPUTER_MARKER
            and board[sq3] == COMPUTER_MARKER
        ):
            return "Computer"

    return None  # Tie


def alternate_player(current_player):
    ''' Return who will be current_player:
    alternates from 'Player' to 'Computer' each turn '''
    return 'Computer' if current_player == 'Player' else 'Player'

def choose_square(board, current_player):
    '''Invoke function to choose_square for the current_player'''
    if current_player == 'Player':
        player_choose_square(board)
    else:
        computer_chooses_square(board)


def someone_won(board):
    """ Return boolean eval of detect_winner()'s value: True if someone won, else False """
    return bool(detect_winner(board))


def display_round(player_score, computer_score):
    ''' Output current score for round for player and computer '''
    print(f"CURRENT SCORE: Player {player_score} | Computer {computer_score}")
    time.sleep(3.8)

def match_won(player_score, computer_score):
    '''Return bool: T is a player won the match, else F'''
    # if (player_score == MATCH_WON) or (computer_score == MATCH_WON):
    if MATCH_WON in [player_score, computer_score]:
        return True
    return False

def display_match_end(winner, match, player_score, computer_score, tie_score):
    ''' Output match results: overall winner, total scores, match rounds'''
    print()
    display_header("MATCH OVER")
    print(f"{winner} wins best out of {match} rounds!\n")
    time.sleep(1.9)
    os.system("clear")
    display_header("FINAL SCORES")
    print(f"Player: {player_score}")
    print(f'Computer: {computer_score}')
    if tie_score != 0:
        print(f"Tie: {tie_score}\n")


def play_again():
    ''' Ask player if they would like to play again:
    y -> new match, n -> terminate game '''
    valid_answer = ['y', 'n']
    while True:
        print()
        prompt("Play again? (y or n)")
        answer = input().casefold()

        if answer == "y":
            os.system("clear")
            play_tic_tac_toe()
            break

        if answer == 'n':
            prompt("Thanks for playing Tic Tac Toe!")
            time.sleep(1.9)
            os.system("clear")
            break

        if answer not in valid_answer:
            error_prompt()


def play_tic_tac_toe():
    """ main entry point """
    match = 1
    player_score = 0
    computer_score = 0
    tie_score = 0
    current_player = FIRST_PLAYER

    intro_prompt()

    if FIRST_PLAYER == 'Choose':
        current_player = choose_first_player(current_player)

    while True:
        board = initialize_board()

        # game round: players take turn choosing square until winner/tie
        while True:
            display_board(board, match)
            choose_square(board, current_player)
            current_player = alternate_player(current_player)
            if someone_won(board) or board_full(board):
                break

        # display board with both player choices
        display_board(board, match)

        if someone_won(board):
            if detect_winner(board) == "Player":
                player_score += 1
            elif detect_winner(board) == "Computer":
                computer_score += 1

            if match_won(player_score, computer_score):
                break

            prompt(f"{detect_winner(board)} won!")

        else:
            prompt("It's a tie!")
            tie_score += 1

        display_round(player_score, computer_score)
        match += 1

    if match_won(player_score, computer_score):
        winner = "Player" if player_score == MATCH_WON else "Computer"
        display_match_end(winner, match, player_score, computer_score, tie_score)
        time.sleep(1.5)
        play_again()

play_tic_tac_toe() # invoke game
