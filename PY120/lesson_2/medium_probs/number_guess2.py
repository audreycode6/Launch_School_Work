'''In the previous exercise, you wrote a number guessing game 
that determines a secret number between 1 and 100, and 
gives the user 7 opportunities to guess the number.

Update your solution to accept a low and high value
when you create a GuessingGame object, and use those 
values to compute a secret number for the game. 
You should also change the number of guesses allowed so the
user can always win if she uses a good strategy. 
You can compute the number of guesses with:
'''
'''TODO:
-accept low and high args for initialzier
    -low = start for range
    -high = stop for range
-change # of guesses allowed so user can always win'''


import random
import math

class GuessingGame:
    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.number_range = range(low, high + 1)
        self.number_of_guesses = int(math.log2(high - low + 1)) + 1
    
    def get_user_guess(self):
        '''get user's guess and handle bad input:
                - non numeric value 
                - not in range 1-100
        '''
        while True: 
            try:
                user_guess = int(input(
                    f"Enter a number in between {self.low} and {self.high}: "))
                if user_guess in self.number_range:
                    return user_guess
                print("Invalid guess.")
            except ValueError:
                print("Invalid guess.")

    def play(self):
        self.answer = random.choice(self.number_range)
        # print(f"TEST: {self.answer}")

        for guess_remaining in range(self.number_of_guesses, 0 , -1):
            print(f"You have {guess_remaining} guesses remaining.")

            self.user_guess = self.get_user_guess()

            if self.user_guess != self.answer: # incorrect guess but in range
                guess_result = 'high' if self.user_guess > self.answer else 'low'
                print(f"Your guess is too {guess_result}.\n")
            else: # correct answer
                print("That's the number!\n")
                break
          
        print(self.display_results())

    def display_results(self):
        game_result = (
            "You have no more guesses. You lost!" 
            if self.user_guess != self.answer
            else "You won!") 
        return game_result


game = GuessingGame(501, 1500)
game.play()
