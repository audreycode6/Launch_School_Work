import random

class Player:
    CHOICES = ('rock', 'paper', 'scissors')

    def __init__(self, player_type):
        self._player_type = player_type.lower()
        self.move = None

    def is_human(self):
        return self._player_type == 'human'

    def choose(self):
        '''returns a string that represents the player's move (option from choices)'''
        if self.is_human():
            prompt = 'Please choose: rock, paper, or scissors. '

            while True:
                choice = input(prompt).lower()
                if choice in Player.CHOICES:
                    break

                print(f'{choice} is not valid, try again.')

            self.move = choice
        else:
            self.move = random.choice(Player.CHOICES)

class Move:
    def __init__(self):
        # TODO seems like we need something to keep track of the choice
        # a move object can be 'paper', 'rock', 'scissors'
        pass

class Rule:
    def __init__(self):
        # TODO not sure what the 'state' of a rule object should be?
        pass

    def compare(self, move1, move2):
        # TODO not sure where 'compare' goes yet
        pass

class RPSGame:
    def __init__(self):
        self._human = Player('human')
        self._computer = Player('computer')

    def display_welcome_message(self):
        print('Welcome to Rock Paper Scissors!')

    def display_goodbye_message(self):
        print("Thanks for playing Rock Paper Scissors. Goodbye!")

    def display_winner(self):
        human_move = self._human.move
        computer_move = self._computer.move

        print(f"You chose : {human_move}")
        print(f"The computer chose: {computer_move}")

        if ((human_move == 'rock' and computer_move == 'scissors') or
            (human_move == 'paper' and computer_move == 'rock') or
            (human_move == 'scissors' and computer_move == 'paper')):

            print("You win!")
        elif ((computer_move == 'rock' and human_move == 'scissors') or
              (computer_move == 'paper' and human_move == 'rock') or
               (computer_move == 'scissors' and human_move == 'paper')):
            
            print("Computer wins!")
        else:
            print("It's a tie.")

    def play(self):
        self.display_welcome_message()
        while True:
            self._human.choose()
            self._computer.choose()
            self.display_winner()
            if not self.play_again():
                break
        self.display_goodbye_message()
    
    def play_again(self):
        answer = input('Want to play again? (y/n): ')
        return answer.lower().startswith('y')
    
        '''better exception handling but wanted to follow ls steps for now vvv
        # valid_input = [['yes', 'yeah', 'y'], ['no', 'nope', 'n']]
        # prompt = 'Want to play again? (y/n): '
        # while True:
        #     play_input = input(prompt).lower()
        #     if play_input in valid_input[0]:
        #         return True
        #     elif play_input in valid_input[1]:
        #         break
        #     print(f"{play_input} is not a valid input.")
        # return False
        '''

RPSGame().play()