
import os
import random

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'

'''format output pretty'''
def prompt(message):
    print(f"==> {message}")

'''board to display in game: formatted and interpolated 
with dictionary awaiting user input'''
def display_board(board):
    # clear board from terminal before displaying new board
    os.system('clear')

    prompt(f'You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.')
    print('')
    print('     |     |')
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print('     |     |')
    print('')

''' return empty dictionary for positions of 3x3 board'''
def initialize_board(): 
    return {square: INITIAL_MARKER for square in range(1, 10)}

''' return list of available (aka INITIAL_MARKER) squares on board'''
def empty_squares(board):
    return [key for key, value in board.items()
            if value == INITIAL_MARKER]

def player_choose_square(board):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f'Choose a square ({', '.join(valid_choices)}):')
        square = input().strip()
        if square in valid_choices:
            break
        
        prompt("Sorry, that's not a valid choice")

    board[int(square)] = HUMAN_MARKER

def computer_chooses_square(board):
    if len(empty_squares(board)) == 0:
        return
    square = random.choice(empty_squares(board))
    board[square] = COMPUTER_MARKER

def board_full(board):
    return len(empty_squares(board)) == 0

'''detect_winner() returns string of winner or falsy None value, 
convert to boolean that is returned'''
def someone_won(board):
    return bool(detect_winner(board)) 

def detect_winner(board):
    winning_lines = [ 
        [1, 2, 3], [4, 5, 6], [7, 8, 9], # horizontal
        [1, 4, 7], [2, 5, 8], [3, 6, 9], # vertical
        [1, 5, 9], [3, 5, 7] # diagonal
    ]

    for line in winning_lines:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARKER
            and board[sq2] == HUMAN_MARKER
            and board[sq3] == HUMAN_MARKER):
            return 'You'
        elif (board[sq1] == COMPUTER_MARKER
            and board[sq2] == COMPUTER_MARKER
            and board[sq3] == COMPUTER_MARKER):
            return 'Computer'
    
    return None # Tie 

'''main entry point:'''
def play_tic_tac_toe():
    while True:
        board = initialize_board() 

        # game round
        while True:
            display_board(board)

            player_choose_square(board)
            if someone_won(board) or board_full(board):
                break

            computer_chooses_square(board)
            if someone_won(board) or board_full(board):
                break

        display_board(board)

        if someone_won(board):
            prompt(f"{detect_winner(board)} won!")
        else: 
            prompt("It's a tie!")

        prompt("Play again? (y or n)")
        answer = input().lower()
        if answer[0] != 'y':
            break 

    prompt('Thanks for playing Tic Tac Toe!')

play_tic_tac_toe()
