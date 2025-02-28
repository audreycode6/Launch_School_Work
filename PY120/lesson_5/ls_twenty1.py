'''Here's our reference implementation. Remember, your solution 
doesn't have to look like this. However, you should investigate
 the design tradeoffs if your design differs in significant ways.
'''
import random
import os

def clear_screen():
    os.system('clear')

class Card:
    SUITS = ("Clubs", "Diamonds", "Hearts", "Spades")
    RANKS = (
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
        "Ace",
    )

    def __init__(self, suit, rank):
        self._suit = suit
        self._rank = rank
        self._hidden = False

    def __str__(self):
        if self._hidden:
            return "Hidden"
        return f"{self.rank} of {self.suit}"

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    @property
    def hidden(self):
        return self._hidden

    def is_ace(self):
        return self.rank == "Ace"

    def is_king(self):
        return self.rank == "King"

    def is_queen(self):
        return self.rank == "Queen"

    def is_jack(self):
        return self.rank == "Jack"

    def is_face_card(self):
        return self.is_king() or self.is_queen() or self.is_jack()

    def hide(self):
        self._hidden = True

    def reveal(self):
        self._hidden = False

class Deck:
    def __init__(self):
        self.cards = [
            Card(suit, rank)
            for suit in Card.SUITS
            for rank in Card.RANKS
        ]
        self.shuffle_cards()

    def shuffle_cards(self):
        random.shuffle(self.cards)

    def deal_card_face_up(self):
        return self.cards.pop()

    def deal_card_face_down(self):
        card = self.deal_card_face_up()
        card.hide()
        return card

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, new_card):
        self.cards.append(new_card)

    def reset(self):
        self.cards = []

    def show(self, caption):
        print(caption)
        for card in self.cards:
            print(card)
        print()

    def reveal_all(self):
        for card in self.cards:
            card.reveal()

    @property
    def total(self):
        total = 0
        for card in self.cards:
            if card.hidden:
                continue
            if card.is_ace():
                total += 11
            elif card.is_face_card():
                total += 10
            else:
                total += int(card.rank)

        # Correct for Aces
        aces = [
            card for card in self.cards
            if card.is_ace() and not card.hidden
        ]
        for _ in aces:
            if total > TwentyOneGame.TARGET_SCORE:
                total -= 10

        return total

    def is_busted(self):
        return self.total > TwentyOneGame.TARGET_SCORE

class Player:
    INITIAL_PURSE = 5
    WINNING_PURSE = 2 * INITIAL_PURSE

    def __init__(self):
        self.hand = Hand()
        self.money = Player.INITIAL_PURSE

    def win_bet(self):
        self.money += 1

    def lose_bet(self):
        self.money -= 1

    def is_broke(self):
        return self.money <= 0

    def is_rich(self):
        return self.money >= Player.WINNING_PURSE

    def show_purse(self):
        print(f"You have ${self.money}")

class Dealer:
    def __init__(self):
        self.hand = Hand()

class TwentyOneGame:
    TARGET_SCORE = 21
    DEALER_MUST_STAY_SCORE = TARGET_SCORE - 4
    HIT = "h"
    STAY = "s"

    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()
        self.deck = None

    def start(self):
        self.display_welcome_message()
        while not self.is_game_over():
            self.play_one_game()
            if not self.play_again():
                break
        self.display_is_game_over_message()
        self.display_goodbye_message()

    def play_one_game(self):
        self.deal_cards()
        self.show_cards()
        self.player.show_purse()
        self.player_turn()

        if not self.player.hand.is_busted():
            self.dealer_turn()

        clear_screen()
        self.show_cards()
        self.display_result()
        self.update_purse()
        self.player.show_purse()

    def deal_cards(self):
        self.deck = Deck()
        self.player.hand.reset()
        self.dealer.hand.reset()

        self.player.hand.add_card(self.deck.deal_card_face_up())
        self.dealer.hand.add_card(self.deck.deal_card_face_up())
        self.player.hand.add_card(self.deck.deal_card_face_up())
        self.dealer.hand.add_card(self.deck.deal_card_face_down())

    def show_cards(self):
        self.dealer.hand.show("Dealer's Cards")
        self.show_score_for(self.dealer.hand)
        self.player.hand.show("Your Cards")
        self.show_score_for(self.player.hand)

    def update_purse(self):
        winner = self.who_won()
        if winner == self.player:
            self.player.win_bet()
        elif winner == self.dealer:
            self.player.lose_bet()

    def show_score_for(self, hand):
        print(f"Points: {hand.total}")
        print()

    def who_won(self):
        if self.player.hand.is_busted():
            return self.dealer
        if self.dealer.hand.is_busted():
            return self.player
        player_score = self.player.hand.total
        dealer_score = self.dealer.hand.total
        if player_score > dealer_score:
            return self.player
        if player_score < dealer_score:
            return self.dealer
        return None

    def display_result(self):
        if self.player.hand.is_busted():
            print("You busted! Dealer wins.")
        elif self.dealer.hand.is_busted():
            print("Dealer busted! You win.")
        else:
            winner = self.who_won()
            if winner == self.player:
                print("You win!")
            elif winner == self.dealer:
                print("Dealer wins!")
            else:
                print("Tie game.")
        print()

    def hit_or_stay(self):
        while True:
            answer = input("Hit or Stay (h/s)? ").lower()
            if answer in [TwentyOneGame.HIT, TwentyOneGame.STAY]:
                return answer
            print("Sorry, that's not a valid choice.")
            print()

    def hit(self, hand):
        hand.add_card(self.deck.deal_card_face_up())
        if hand.is_busted():
            return
        clear_screen()
        self.show_cards()

    def player_turn(self):
        while self.hit_or_stay() == TwentyOneGame.HIT:
            self.hit(self.player.hand)
            if self.player.hand.is_busted():
                break

    def dealer_turn(self):
        self.dealer.hand.reveal_all()
        clear_screen()
        self.show_cards()

        while True:
            score = self.dealer.hand.total
            if (score >= TwentyOneGame.DEALER_MUST_STAY_SCORE or
                    self.dealer.hand.is_busted()):
                break
            input("Press Return to continue...")
            self.hit(self.dealer.hand)

    def play_again(self):
        while True:
            answer = input("Play again (y/n)? ").lower()
            if answer in ["y", "n"]:
                break
            print("Sorry, that's not a valid choice.")
            print()
        clear_screen()
        return answer == "y"

    def display_welcome_message(self):
        print("Welcome to 21!")
        print()

    def display_goodbye_message(self):
        print("Thanks for playing 21! Goodbye!")
        print()

    def is_game_over(self):
        return self.player.is_broke() or self.player.is_rich()

    def display_is_game_over_message(self):
        if self.player.is_broke():
            print("You're broke!")
        elif self.player.is_rich():
            print("You're rich!")

# Running the game
game = TwentyOneGame()
game.start()