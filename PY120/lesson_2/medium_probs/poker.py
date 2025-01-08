'''In the previous two exercises, 
you developed a Card class and a Deck class. 
You are now going to use those classes to create 
and evaluate poker hands. Create a class, PokerHand, 
that takes 5 cards from a Deck of Cards and evaluates 
those cards as a poker hand.'''


import random

class Card:
    RANK_VALUES = {'Jack': 11, 'Queen' : 12, 'King' : 13, 'Ace': 14}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    @property
    def value(self):
        return Card.RANK_VALUES.get(self.rank, self.rank)

    def __lt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.value < other.value

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.rank == other.rank and self.suit == other.suit

    def __str__(self):
        '''returns a string representation of the card.'''
        return f"{self.rank} of {self.suit}" 

class Deck:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

    def __init__(self):
        self._get_shuffled_deck()

    def draw(self):
        '''remove and return a card from deck'''
        if not self._deck:
            self._get_shuffled_deck()
        return self._deck.pop()
    
    def _get_shuffled_deck(self):
        '''create deck of cards and shuffle them'''
        self._deck = [Card(rank, suit) 
                    for suit in Deck.SUITS 
                    for rank in Deck.RANKS
                    ]
        random.shuffle(self._deck)

# NEW
class PokerHand:

    def __init__(self, deck):
        self._hand = [deck.draw() for _ in range(5)]
        self._hand_suits = [card.suit for card in self._hand] 
        self._hand_ranks = [card.rank for card in self._hand] 
        self._sorted_hand_values = sorted([card.value for card in self._hand])
        self._min_value = self._sorted_hand_values[0]
        self._max_value = self._sorted_hand_values[-1]     


    def print(self):
       '''print each card in hand'''
       for card in self._hand:
           print(card)

    def evaluate(self):
        if self._is_royal_flush():
            return "Royal flush"
        elif self._is_straight_flush():
            return "Straight flush"
        elif self._is_four_of_a_kind():
            return "Four of a kind"
        elif self._is_full_house():
            return "Full house"
        elif self._is_flush():
            return "Flush"
        elif self._is_straight():
            return "Straight"
        elif self._is_three_of_a_kind():
            return "Three of a kind"
        elif self._is_two_pair():
            return "Two pair"
        elif self._is_pair():
            return "Pair"
        else:
          return "High card"

    def _is_royal_flush(self):
        ''''check if hand is all royalty ranks and have same suit'''
        royal_ranks = ['Ace', 'King', 'Queen', 'Jack', 10]
        if PokerHand._is_flush(self):
            for rank in self._hand_ranks:
                if rank in royal_ranks:
                    royal_ranks.remove(rank)
                    continue
            return royal_ranks == []

    def _is_straight_flush(self):
        ''' check if hand is 5 cards in sequence'''
        return PokerHand._is_flush(self) and PokerHand._is_straight(self)

    def _is_four_of_a_kind(self):
        '''all 4 suits of same rank'''
        for rank in self._hand_ranks:
            if self._hand_ranks.count(rank) == 4:
                return True
        
    def _is_full_house(self):
        '''3 of a kind with a pair'''
        for rank in self._hand_ranks:
            if self._hand_ranks.count(rank) in [2, 3]:
                continue
            return False
        return True

    def _is_flush(self):
        '''check  hand has all same suit'''
        return PokerHand._matches_set_length(self, self._hand_suits, 1)
  
    def _is_straight(self):
        '''check hand is sequence (increment values of 1)'''
        value_range = list(range(self._min_value, self._max_value +1))
        return self._sorted_hand_values == value_range
        
    def _is_three_of_a_kind(self):
        '''3 cards of same rank, other 2 dont matter'''
        for rank in self._hand_ranks:
            if self._hand_ranks.count(rank) == 3:
                return True
            else:
                continue

    def _is_two_pair(self):
        '''2 diff pairs of same rank - 1 doesnt matter'''
        return PokerHand._matches_set_length(self, self._hand_ranks, 3)


    def _is_pair(self):
        '''2 cards have same rank, other 3 dont matter'''
        return PokerHand._matches_set_length(self, self._hand_ranks, 4)
    
    def _matches_set_length(self, lst, length):
        '''helper func to check that list of card info,
        converted to its set length is == to length arg'''
        return len(set(lst)) == length


# TESTING:
hand = PokerHand(Deck()) 
hand.print() # print hand -> 5 cards
print(hand.evaluate()) # eval hand
print()

# Adding TestDeck class for testing purposes

class TestDeck(Deck):
    def __init__(self, cards):
        self._deck = cards

# All of these tests should return True

hand = PokerHand(
    TestDeck(
        [
            Card("Ace", "Hearts"),
            Card("Queen", "Hearts"),
            Card("King", "Hearts"),
            Card("Jack", "Hearts"),
            Card(10, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Royal flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Clubs"),
            Card("Queen", "Clubs"),
            Card(10, "Clubs"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight flush")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Four of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Full house")

hand = PokerHand(
    TestDeck(
        [
            Card(10, "Hearts"),
            Card("Ace", "Hearts"),
            Card(2, "Hearts"),
            Card("King", "Hearts"),
            Card(3, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Diamonds"),
            Card(10, "Clubs"),
            Card(7, "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card("Queen", "Clubs"),
            Card("King", "Diamonds"),
            Card(10, "Clubs"),
            Card("Ace", "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(6, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Three of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(9, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(8, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Two pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card("King", "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "High card")