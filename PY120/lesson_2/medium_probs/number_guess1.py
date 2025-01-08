'''Create an object-oriented number guessing class 
for numbers in the range 1 to 100, with a limit of 7
guesses per game.

Note that a game object should start a new game
with a new number to guess with each call to play.
  
The game should play like this:'''

'''TODO:
-create GuessingGames class
- numbers range 1-100
- limit 7 guessing per game
    -need to track/update each guess
- play method:
    - when called on GuessingGame object create new random answer (# in range 1-100 inclusive)
        - random module (?)
    -prompts:
        -f"You have {guess_count} guesses remaining."
        - get input: user_guess = input('Enter a number between 1 and 100: ")
        - display results:
            - if user_guess not in range -> try catch: 'Invalid guess." getinput again
            - if valid guess range but not correct answer:
                - update guess_count -1
                - give feedback: "Your guess is too {low/high}
            - if correct guess:
                -display feedback: 'That's the number!"
                - terminate game and display final result: "You won!"
                
            - check how many guesses remaininig: 
                - if guesses remaining > 0: continye above cycle
                -else: "You have no more guesses. You lost!" and terminate game

'''
import random
class GuessingGame:
    NUMBER_RANGE = range(1,101)
    MAX_GUESSES = 7

    def __init__(self):
        self.answer = None
        self.guess_count = GuessingGame.MAX_GUESSES
        self.user_guess = None
    
    def get_user_guess(self):
        '''get user's guess and handle bad input:
                - non numeric value 
                - not in range 1-100
        '''
        while True: 
            try:
                user_guess = int(input("Enter a number in between 1 and 100: "))
                if user_guess in GuessingGame.NUMBER_RANGE:
                    return user_guess
                print("Invalid guess.")
            except ValueError:
                print("Invalid guess.")

    def play(self):
        '''play guessing game:
            - new random answer stored for game
            - display how many guesses remaining (guess_count)
            - get users guess: (helper func: get_user_guess())
                - while their guess != answer OR 
                - until they run out of guess attempts
            - display game results (helper func: display_results())
        '''
        self.answer = random.choice(GuessingGame.NUMBER_RANGE)
        # print(f"TEST: {self.answer}")

        for guess_remaining in range(self.guess_count, 0, -1):
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


game = GuessingGame()
game.play() 
