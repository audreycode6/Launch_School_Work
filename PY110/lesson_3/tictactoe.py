''' Tiktactoe game: User plays on terminal with computer.
Computer plays offensively and defensively. 
Player to get their score == MATCH_WON wins match.'''

import os
import random
import time

# FIRST_PLAYER: alter to change who the first player is
#     'None' == players picks who goes first,
#     'Player' == player goes first
#     'Computer' == computer goes first
FIRST_PLAYER = None # or 'Player' or 'Computer'
INITIAL_MARKER = " "
HUMAN_MARKER = "X"
COMPUTER_MARKER = "O"
PLAYER_WIN = ['X', 'X', 'X']
COMPUTER_WIN = ['O', 'O', 'O']
EXAMPLE_BOARD = {num: num for num in range(1,10)}
FIRST_ROUND = 1
CENTER_SQUARE = 5
MATCH_WON = 3 # alter to change number of wins needed to win match
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
    print(f"\n    * {message} *    \n")


def error_prompt():
    ''' Output error message for invalid input '''
    print('\n!!! ERROR: Invalid input, try again. !!! \n')


def intro_prompt():
    ''' Output welcome message, intro, and objective of game. '''

    display_header("WELCOME TO TIC TAC TOE")
    prompt('Each round you will be asked to pick a'
           ' number that aligns with the positions in the box grid. \n')
    print('EXAMPLE BOARD:')
    display_board(EXAMPLE_BOARD, 'Example', False)
    prompt('Get 3 of your marks in a line (vertically, horizontally, or diagonally).')
    prompt(f"First player to reach {MATCH_WON} wins, wins the match! \n")
    time.sleep(1)
    input("==> Press 'Enter' to continue.")


def initialize_board():
    """ Return empty dictionary for positions of 3x3 board """
    return {square: INITIAL_MARKER for square in range(1, 10)}


def display_board(board, match, display=True):
    """ Output board to display in game: formatted and interpolated
    with dictionary awaiting user input """
    if display:
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
    ('Computer' or 'Player')
    After match starts players will alternate turns until the match ends.
    '''
    while True:
        print()
        prompt('Choose which player will start the match. Enter C for computer or P for yourself.')
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

def comp_protect(line, board, marker):
    '''computer choose best choice: 
    return square number if chance for offense (marker = COMPUTER...)
    or chance to defend (marker = HUMAN...)
    else None'''
    markers_in_line = [board[square] for square in line]

    if markers_in_line.count(marker) == 2:
        for square in line:
            if board[square] == INITIAL_MARKER:
                return square
    return None


def computer_chooses_square(board):
    ''' Update board with computers choice:
    options in order of priority:
        offense move,
        defense moove,
        center square,
        or random '''
    square = None

    for line in WINNING_LINES:
        square = comp_protect(line, board, COMPUTER_MARKER)
        if square: # offense opportunity
            break

    if not square:
        for line in WINNING_LINES:
            square = comp_protect(line, board, HUMAN_MARKER)
            if square: # defend
                break

    if not square:
        if board[CENTER_SQUARE] == INITIAL_MARKER:
            square = CENTER_SQUARE
        else:
            square = random.choice(empty_squares(board))

    board[square] = COMPUTER_MARKER

def board_full(board):
    ''' Return bool if board has empty squares or not '''
    return len(empty_squares(board)) == 0

def check_winning_line(board, line):
    '''helper func to detect winner:
    determine if winning line on board is all player markers
    or computer markers, if none it is a tie. return the result'''
    current_line = [board[elem] for elem in line]
    if current_line == PLAYER_WIN:
        return 'Player'
    if current_line == COMPUTER_WIN:
        return 'Computer'
    return None


def detect_winner(board):
    """ Return string of winner or None if tie """
    for line in WINNING_LINES:
        line_result = check_winning_line(board, line)
        if line_result is not None:
            return line_result
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

def player_points(round_winner, player_score, computer_score):
    ''' increase winning players score and return scores so
    that play_tic_tac_toe() keeps track of scores '''
    if round_winner == "Player":
        player_score += 1
    elif round_winner == "Computer":
        computer_score += 1
    return player_score, computer_score


def display_round(player_score, computer_score):
    ''' Output current score for round for player and computer '''
    print(f"CURRENT SCORE: Player {player_score} | Computer {computer_score}")
    time.sleep(1.9)

def match_won(player_score, computer_score):
    '''Return bool: T is a player won the match, else F'''
    return MATCH_WON in [player_score, computer_score]


def display_match_end(winner, match, player_score, computer_score, tie_score):
    ''' Output match results: overall winner, total scores, match rounds'''
    display_header("MATCH OVER")
    print(f"{winner} wins best out of {match} rounds!")
    time.sleep(1.9)
    os.system("clear")
    display_header("FINAL SCORES")
    print(f"Player: {player_score}")
    print(f'Computer: {computer_score}')
    if tie_score != 0:
        print(f"Tie: {tie_score}\n")


def play_again():
    ''' Ask player if they would like to play again:
        - y -> new match
        - n -> terminate game 
    '''
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

    if FIRST_PLAYER is None:
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
            winner = detect_winner(board)
            if winner in ['Player', 'Computer']:
                player_score, computer_score = player_points(winner, player_score, computer_score)
            if match_won(player_score, computer_score):
                break
            prompt(f"{winner} won!")

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
