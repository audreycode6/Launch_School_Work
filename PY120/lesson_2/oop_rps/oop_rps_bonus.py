import random

class Player:
    CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    VALID_CHOICE_INPUT = {
        'r' : 'rock', 
        'p': 'paper', 
        'sc': 'scissors' ,
        'l': 'lizard', 
        'sp': 'spock'
        }

    def __init__(self):
        self.move = None
        self.move_history = {choice: 0 for choice in Player.CHOICES}

    def update_and_display_move_history(self):
        self.move_history[self.move] += 1
        print(f"{self.__class__.__name__} Moves:")
        for choice, count in self.move_history.items():
            if count > 0:
                print(f"    {choice}: {count}")

    def reset_move_history(self):
        self.move_history.clear()
        self.move_history = {choice: 0 for choice in Player.CHOICES}


class Computer(Player):
    ROBOT_NAMES = ['Robot Rocky',
            'Robot Randy', 
            'Robot John', 
            'Robot Boots']

    def __init__(self):
        super().__init__()
        self.name = random.choice(self.ROBOT_NAMES)

    def choose(self, previous_move):
        if self.name == 'Robot Rocky':
            self.move = 'rock'
        elif self.name == 'Robot Boots':
            if previous_move:
                self.move = previous_move
            else:
                self.move = random.choice(Player.CHOICES)
        elif self.name == 'Robot John':
            self.move = random.choice(['rock', 'paper', 'scissors'])
        else: # 'Randy'
            self.move = random.choice(Player.CHOICES)

    def reset_name(self):
        self.name = random.choice(self.ROBOT_NAMES)

class Human(Player):
    def __init__(self):
        super().__init__()
        self.previous_move = None

    def choose(self):
        prompt = (f"\n==> Please choose {', '.join(Player.CHOICES[:4])},"""
        f""" or {Player.CHOICES[-1]}: """)
        while True:
            choice = input(prompt).lower()
            if choice.lower() in Player.VALID_CHOICE_INPUT: # abbreviated input
                choice = Player.VALID_CHOICE_INPUT[choice.lower()]
                break
            if choice.lower() in Player.CHOICES:
                break
            print(f"!! Sorry, {choice} is not valid !!")
        self.move = choice


class RPSGame:
    game_title = ' '.join(Player.CHOICES).title()

    def __init__(self):
        self._human = Human()
        self._computer = Computer()
        self._score = Score(self._computer)
        self.previous_move = None

    def display_welcome_message(self):
        print(f"** Welcome to {self.game_title}! **")

    def display_goodbye_message(self):
        print(f"** Thanks for playing {self.game_title}. Goodbye! **")

    def display_rules(self):
        rule_intro = (
        f"\nRules:\n"
        f"   * First player to reach {self._score.MAX_SCORE} points wins!\n"
        "   * At your turn, enter a weapon of choice.\n"
        "   TIP: Full name of the weapon or abbreviations \n"
        "   (r, p, sc, l, sp) are acceptable input."
        )

        move_eval = (
            "\nMove Choices & Evaluation:\n"
            "   * rock * beats lizard and scissors\n"
            "   * paper * beats rock and spock\n"
            "   * scissors * beats paper and lizard\n"
            "   * lizard * beats spock and paper\n"
            "   * spock * beats rock and scissors\n"
            )
        print(rule_intro, move_eval)

    def get_move_instance(self, player_move):
        """Return an instance of the appropriate Move subclass."""
        moves = {
            'rock' : Rock,
            'paper': Paper,
            'scissors': Scissors,
            'lizard' : Lizard,
            'spock': Spock
        }
        return moves[player_move](player_move)

    def get_winner(self):
        human_move = self.get_move_instance(self._human.move)
        computer_move = self.get_move_instance(self._computer.move)

        if self._human.move == self._computer.move:
            return 'tie'
        if human_move.beats(computer_move):
            return 'human'
        return f'{self._computer.name}'

    def _update_and_display_winner(self):
        print(f"You chose: {self._human.move}")
        print(f"{self._computer.name} chose: {self._computer.move}\n")
        winner = self.get_winner()

        if winner == 'human':
            result = 'You win'
            self._score.increment_human()
        elif winner == self._computer.name:
            result = f"{self._computer.name} wins"
            self._score.increment_computer()
        else:
            result = "It's a tie"

        print(f"{result} this round.")

    def play(self):
        self.display_welcome_message()
        self.display_rules()
        while True:
            self._human.choose()
            self._computer.choose(self.previous_move)
            self.previous_move = self.human_previous_move()
            self._update_and_display_winner()
            self._score.display_round()
            self._human.update_and_display_move_history()
            self._computer.update_and_display_move_history()
            if self._score.is_game_over():
                break
        if self.play_again():
            self._score.reset()
            self._computer.reset_name() # new computer player
            self.play()
        else:
            self.display_goodbye_message()
            self._human.reset_move_history()
            self._computer.reset_move_history()

    def human_previous_move(self):
        return self._human.move

    def play_again(self):
        valid_input = [['yes', 'yeah', 'y'], ['no', 'nope', 'n']]
        prompt = '\n==> Want to play again? (y/n): '
        while True:
            play_input = input(prompt).lower()
            if play_input in valid_input[0]:
                return True
            if play_input in valid_input[1]:
                return False
            print(f"{play_input} is not a valid input.")


class Score:
    MAX_SCORE = 5
    def __init__(self, computer):
        self.human = 0
        self.computer = 0
        self.computer_player = computer

    def reset(self):
        self.human = 0
        self.computer = 0

    def increment_human(self):
        self.human += 1

    def increment_computer(self):
        self.computer += 1

    def is_game_over(self):
        return self.MAX_SCORE in (self.computer, self.human)

    def display_round(self):
        player_scores = (f"You: {self.human} | """
                        f"""{self.computer_player.name}: {self.computer} """)
        if not self.is_game_over():
            print(f"CURRENT SCORE: {player_scores} \n")
        else:
            print("\n...game over...\n")
            print(f'FINAL SCORE:\n{player_scores}')
            winner = ('You' if self.human == self.MAX_SCORE
                            else f'{self.computer_player.name}')
            print(f'{winner} won!\n')


class Move:
    def __init__(self, name):
        self.name = name

    def beats(self, other):
        pass

class Rock(Move):
    def beats(self, other):
        return other.name in ['lizard', 'scissors']

class Paper(Move):
    def beats(self, other):
        return other.name in ['rock', 'spock']

class Scissors(Move):
    def beats(self, other):
        return other.name in ['paper', 'lizard']

class Lizard(Move):
    def beats(self, other):
        return other.name in ['spock', 'paper']

class Spock(Move):
    def beats(self, other):
        return other.name in ['rock', 'scissors']


RPSGame().play() # main entry point
