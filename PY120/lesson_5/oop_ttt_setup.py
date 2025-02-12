import random
import os

def clear_screen():
    os.system("clear")

class Square:
    INITIAL_MARKER = ' '
    HUMAN_MARKER = 'X'
    COMPUTER_MARKER = 'O'

    def __init__(self, marker=INITIAL_MARKER):
        self.marker = marker

    def __str__(self):
        return self.marker

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, marker):
        self._marker = marker

    def is_unused(self):
        return self.marker == Square.INITIAL_MARKER

class Board:
    def __init__(self):
        self.reset()

    def reset(self):
        self.squares = {key: Square() for key in range(1,10)}

    def count_markers_for(self, player, keys):
        markers = [self.squares[key].marker for key in keys]
        return markers.count(player.marker)

    def display(self):
        print()
        print("     |     |")
        print(f"  {self.squares[1]}  |"
              f"  {self.squares[2]}  |  {self.squares[3]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[4]}  |"
              f"  {self.squares[5]}  |  {self.squares[6]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[7]}  |"
              f"  {self.squares[8]}  |  {self.squares[9]}")
        print("     |     |")
        print()

    def display_with_clear(self):
        clear_screen()
        print()
        self.display()

    def mark_square_at(self, key, marker):
        self.squares[key].marker = marker

    def unused_squares(self):
        return [key
                for key, square in self.squares.items()
                if square.is_unused()]

    def is_unused_square(self, key): #NEW
        return self.squares[key].is_unused()

    def is_full(self):
        return len(self.unused_squares()) == 0

class Player:
    def __init__(self, marker):
        self.marker = marker
        self._score = 0

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    def increment_score(self):
        self.score += 1

class Human(Player):
    def __init__(self):
        super().__init__(Square.HUMAN_MARKER)

class Computer(Player):
    def __init__(self):
        super().__init__(Square.COMPUTER_MARKER)

class TTTGame:
    POSSIBLE_WINNING_ROWS = (
        (1, 2, 3), # vertical rows
        (4, 5 ,6),
        (7, 8, 9),
        (1, 4, 7), # horizontal rows
        (2, 5, 8),
        (3, 6, 9),
        (1, 5, 9), # diagonal rows
        (3, 5, 7)
    )
    MATCH_GOAL = 3

    @staticmethod
    def _join_or(choices_list, seperator=', ', end='or'):
        length = len(choices_list)
        last_choice = choices_list[-1]
        if length == 1:
            return last_choice
        if length == 2:
            return f"{choices_list[0]} {end} {last_choice}"
        all_but_last = seperator.join(choices_list[:length-1])
        return f"{all_but_last}{seperator}{end} {last_choice}"

    def __init__(self):
        self.human = Human()
        self.computer = Computer()
        self.board = Board()
        self.starting_player = "human"

    def play(self):
        '''main entry'''
        self.display_welcome_message()
        self.play_match()
        self.display_goodbye_message()

    def play_match(self):
        while not self.is_match_over():
            self.play_single_game()
            self.display_score()
            self.switch_starting_player()
            if not self.is_match_over():
                if not self.play_again():
                    break
                clear_screen()

        if self.is_match_over():
            self.display_match_results()

    def play_single_game(self):
        self.board.reset()

        if self.starting_player == "human":
            self.human_starts_play()
        else:
            self.computer_starts_play()

        self.board.display_with_clear()
        self.increment_winners_score()
        self.display_round_winner()

    def switch_starting_player(self):
        self.starting_player = (
            "computer" if self.starting_player == "human"
            else "human")

    def human_starts_play(self):
        self.board.display()
        while True:
            self.human_moves()
            if self.is_game_over():
                break

            self.board.display_with_clear()
            self.computer_moves()
            if self.is_game_over():
                break
            self.board.display_with_clear()

    def computer_starts_play(self):
        while True:
            self.computer_moves()
            if self.is_game_over():
                break

            self.board.display_with_clear()
            self.human_moves()
            if self.is_game_over():
                break
            self.board.display_with_clear()
        self.board.display()

    def play_again(self):
        while True:
            playing_choice = input("\n==> Want to play again? (y/n): ").lower()
            if playing_choice in ['y', 'n']:
                break
            print('Invalid Input! Expecting "y" for yes or "n" for no.')
        return playing_choice == 'y'

    def display_welcome_message(self):
        clear_screen()
        print("* Welcome to Tic Tac Toe! *")
        print(f"\nFirst player to earn {TTTGame.MATCH_GOAL}"
              " points wins the match!")

    def display_goodbye_message(self):
        print("\nThanks for playing Tic Tac Toe! Goodbye!")

    def display_score(self):
        if not self.is_match_over():
            print("\n* CURRENT SCORE *")
        else:
            print("\n... game over ...\n"
              "\n* FINAL RESULTS *")
        print(f"you: {self.human.score} | "
              f"computer: {self.computer.score}")

    def display_round_winner(self):
        if self.is_winner(self.human):
            print("You won! Congratulations!")
        elif self.is_winner(self.computer):
            print("I won! I won! Take that, human!")
        else:
            print("A tie game. How boring.")

    def display_match_results(self):
        self.board.display_with_clear()
        self.display_score()
        winner = ('You' if self.human.score > self.computer.score
                  else 'Computer')
        print(f"{winner} won the match!")

    def increment_winners_score(self):
        if self.is_winner(self.human):
            self.human.increment_score()
        elif self.is_winner(self.computer):
            self.computer.increment_score()

    def human_moves(self):
        choice = None
        valid_choices = self.board.unused_squares()
        while True:
            choices_list = [str(choice) for choice in valid_choices]
            choices_str = TTTGame._join_or(choices_list)
            prompt = f"==> Choose a square ({choices_str}): "
            choice = input(prompt)
            try:
                choice = int(choice)
                if choice in valid_choices:
                    break
            except ValueError:
                pass

            print("Sorry, that's not a valid choice.\n")

        self.board.mark_square_at(choice, self.human.marker)

    def computer_moves(self):
        choice = self.offensive_computer_move()
        if not choice:
            choice = self.defensive_computer_move()
        if not choice:
            choice = self.pick_center_square()
        if not choice:
            choice = self.pick_random_square()

        self.board.mark_square_at(choice, self.computer.marker)

    def pick_center_square(self):
        return 5 if self.board.is_unused_square(5) else None

    def pick_random_square(self):
        valid_choices = self.board.unused_squares()
        return random.choice(valid_choices)

    def critical_square(self, row, player):
        if self.board.count_markers_for(player, row) == 2:
            for mark in row:
                if mark in self.board.unused_squares():
                    return mark
        return None

    def find_critical_square(self, player):
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            square_to_defend = self.critical_square(row, player)
            if square_to_defend:
                return square_to_defend
        return None

    def offensive_computer_move(self):
        return self.find_critical_square(self.computer)

    def defensive_computer_move(self):
        return self.find_critical_square(self.human)

    def is_winner(self, player):
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            if self.three_in_a_row(player, row):
                return True
        return False

    def is_match_over(self):
        return TTTGame.MATCH_GOAL in [self.human.score, self.computer.score]

    def is_game_over(self):
        return self.board.is_full() or self.someone_won()

    def three_in_a_row(self, player, row):
        return self.board.count_markers_for(player, row) == 3

    def someone_won(self):
        return (self.is_winner(self.human) or
        self.is_winner(self.computer))

game = TTTGame()
game.play()