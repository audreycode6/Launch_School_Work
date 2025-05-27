'''Scrabble Score:
Write a program that, given a word, computes the Scrabble score for that word.

Letter Values

You'll need the following tile scores:

Letter	Value
A, E, I, O, U, L, N, R, S, T	1
D, G	2
B, C, M, P	3
F, H, V, W, Y	4
K	5
J, X	8
Q, Z	10

How to Score: Sum the values of all the tiles used in each word. 


'''

'''PEDAC:
P:
    -in: string
    -out: integer
        - 0  if no letter chars (i.e char not in score dict) or not a string
    -e:
    -i:
        - chars are case insenstive (so make lower or casefold)
        - Scrabble class
            - score method returns int of score
    
E: test_scrabble.py
D:
    - dict to map chars as key and count as value for word
    - dict to map the value of letters
'''

class Scrabble:
    LETTERS_SCORE = {
          'aeioulnrst' : 1, 
          'dg' : 2,
          'bcmp' : 3,
          'fhvwy' : 4,
          'k' : 5,
          'jx' : 8,
          'qz' : 10
    }

    def __init__(self, string):
        self.string = string if string else '' # handle None input

    def score(self):
        return Scrabble.calculate_score(self.string)

    @classmethod
    def calculate_score(cls, string):
        total_score = 0
        for char in string.lower(): # case insensitve
            if char.isalpha(): # only check alphabetical chars
                for letters, score in Scrabble.LETTERS_SCORE.items():
                    if char in letters:
                        total_score += score
        return total_score

print(Scrabble.calculate_score('frog')) #  8