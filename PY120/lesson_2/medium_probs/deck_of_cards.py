'''Using the Card class from the previous exercise,
create a Deck class that contains all of the
standard 52 playing cards. 
Use the following code to start your work:'''

import random

class Card:
    RANK_VALUES = {'Jack': 11, 'Queen' : 12, 'King' : 13, 'Ace': 14}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    @property
    def value(self):
        '''convert all card ranks to numeric value
        so that they can be compared properly'''
        return Card.RANK_VALUES.get(self.rank, self.rank)

    def __lt__(self, other):
        '''use < to compare self.value and other.value directly. 
        for min(), max().'''
        if not isinstance(other, Card):
            return NotImplemented
        return self.value < other.value

    def __eq__(self, other):
        '''when using min()/max() 
        compare the rank and suit attributes
        instead of the memory addresses.'''
        if not isinstance(other, Card):
            return NotImplemented
        return self.rank == other.rank and self.suit == other.suit

    def __str__(self):
        '''returns a string representation of the card.'''
        return f"{self.rank} of {self.suit}" 

class Deck():
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

    # NEW 
    def __init__(self):
        self._get_shuffled_deck()

    def draw(self):
        '''remove and return a card from deck'''
        if not self._deck: # if current deck is empty, make new deck + shuffle it,
            self._get_shuffled_deck()
        return self._deck.pop()
    
    def _get_shuffled_deck(self):
        '''create deck of cards and shuffle them'''
        self._deck = [Card(rank, suit) 
                    for suit in Deck.SUITS 
                    for rank in Deck.RANKS
                    ]
        random.shuffle(self._deck)

'''The Deck class should provide a draw method
to deal one card. The Deck should be shuffled
when it is initialized. If no more cards remain
when draw is called, the method should generate a
new set of 52 shuffled cards, 
then deal one card from the new cards.'''

deck = Deck()
drawn = []
for _ in range(52):
    drawn.append(deck.draw())

count_rank_5 = sum([1 for card in drawn if card.rank == 5])
count_hearts = sum([1 for card in drawn if card.suit == 'Hearts'])

print(count_rank_5 == 4)      # True
print(count_hearts == 13)     # True

drawn2 = []
for _ in range(52):
    drawn2.append(deck.draw())

print(drawn != drawn2)        # True (Almost always).
'''Note that the last line should almost always print "True";
if you shuffle the deck 1000 times a second, 
you will be very, very, very old before you see two consecutive
shuffles produce the same results. 
If you get a "False" result, you almost certainly 
have something wrong.'''