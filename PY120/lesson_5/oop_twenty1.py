import os
import random

def clear_screen():
    os.system("clear")

class Deck:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
    def __init__(self):
        self.reset()

    def deal(self, number_of_cards=2):
        '''returns list with (number_of_cards) cards as elements
        choosen randomly from deck 
        and removes them from deck '''
        cards_dealt = []
        for _ in range(number_of_cards):
            try:
                card = random.choice(self.deck)
                self.deck.remove(card)
                cards_dealt.append(card)
            except IndexError:
                print("Ran out of cards in deck!")
                # TODO maybe unneccesary

        return cards_dealt
        # print(f"\nLEngth: {len(self.deck)}")
        # print(f"\n AFTER:{ self.deck}")
        # print(f"    TEST cards to deal: {cards}\n")

    def reset(self):
        self.deck = [f'{rank} of {suit}'
                     for suit in Deck.SUITS
                     for rank in Deck.RANKS
                    ]

class Participant():
    def __init__(self):
        self.score = 0
        self.hand = []

    def hit(self, current_deck):
        new_card = current_deck.deal(1)
        self.hand.append(new_card[0])
        clear_screen()
        print(f"{new_card[0]} was added!")

    def display_hand(self, player="You have"):
        hand_size = len(self.hand)
        if hand_size == 2:
            return f"{player}: {" and ".join(self.hand)}"

        last_card = self.hand[-1]
        all_but_last_card = self.hand[:-1]
        return f"{player}: {", ".join(all_but_last_card)}, and {last_card}"

    def stay(self):
        pass

    def is_busted(self):
        return self.score > 21

    def current_score(self):
        self.score = 0
        for card in self.hand:
            cards = card.split()
            rank = cards[0]
            if rank in ["Jack", "Queen", "King"]:
                value = 10
            elif rank == "Ace":
                value = 11
            # TODO figure out how to change to 1 if needed (score > 21)
            else:
                value = int(rank)

            self.score += value
        return self.score

class Player(Participant):
    def __init__(self):
        super().__init__()
        self.betting_balance = 5

    def is_busted(self):
        return self.current_score() > 21

    def stay(self):
        clear_screen()
        print("* You chose to stay! *")
        print("\n... Dealers turn ...\n")

    def update_money(self, player_won):
        if player_won:
            self.betting_balance += 1
            print("You earned another dollar!")
        else:
            self.betting_balance -= 1
            print("You lost a dollar!")

    def display_money_available(self):
        print(f"You have ${self.betting_balance} for betting.")

class Dealer(Participant):
    def __init__(self):
        super().__init__()

    def hit(self, current_deck):
        new_card = current_deck.deal(1)
        self.hand.append(new_card[0])
        print("* Dealer has hit *")

    def stay(self):
        print("* Dealer chose to stay *")

    def display_hidden_hand(self, player="Dealer has"):
        one_card = self.hand[0]
        return f"{player}: {one_card} and unknown card"

    def reveal_hand(self):
        return super().display_hand("Dealer's Hand")

    def deal(self):
        # STUB
        pass

class TwentyOneGame:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()
        self.playing = True
        self.match_over = False

    def start(self):
        self.display_welcome_message()
        while True:
            self.play_single_game()
            self.display_result_update_money()
            self.match_over = self.is_match_over()
            if not self.match_over:
                self.playing = self.play_again()
            if (not self.playing or
                self.match_over):
                break
            self.reset_game()

        if self.match_over:
            self.display_match_results()
        self.display_goodbye_message()

    def play_single_game(self):
        self.player.display_money_available()
        self.deal_cards()
        self.player_turn()
        if not self.player.is_busted():
            self.dealer_turn()

    def is_match_over(self):
        return self.player.betting_balance in [0, 10]

    def reset_game(self):
        '''reset player scores & hands, and deck + terminal'''
        self.player.score = 0
        self.dealer.score = 0
        self.deck.reset()
        self.player.hand.clear()
        self.dealer.hand.clear()
        clear_screen()

    def display_match_results(self):
        print("... GAME OVER ...\n")
        if self.match_over:
            if self.player.betting_balance == 10:
                print("You're too good at this game! Take your money and go.")
            else:
                print("You're broke... No money, no playing!")

    def deal_cards(self):
        for card in self.deck.deal():
            self.player.hand.append(card)
        for card in self.deck.deal():
            self.dealer.hand.append(card)

    def show_cards(self):
        print()
        print(self.dealer.display_hidden_hand())
        print(self.player.display_hand())

    def player_turn(self):
        prompt = "==> Would you like to hit or stay? (h/s): "
        while True:
            self.show_cards()
            print(f"You currently have {self.player.current_score()} points\n")

            while True:
                hit_or_stay = input(prompt).lower()
                if hit_or_stay in ['h', 's']:
                    break
                print("\n!!   Invalid Input: Enter 'h' to hit"
                    " and add another card to your deck "
                    "\nor 's' to stay and keep the hand"
                    " you have   !!\n")

            if hit_or_stay == 's':
                self.player.stay()
                break
            if hit_or_stay == "h":
                self.player.hit(self.deck)
                if self.player.is_busted():
                    break

    def dealer_turn(self):
        while self.dealer.current_score() < 17:
            self.dealer.hit(self.deck)
        if not self.dealer.is_busted():
            self.dealer.stay()
        input("\n==> Press Enter to see the results: ")
        clear_screen()

    def determine_winner(self):
        player_score = self.player.current_score()
        dealer_score = self.dealer.current_score()
        if (
            (player_score > 21 and dealer_score > 21) or
            (player_score == dealer_score)
            ):
            winner = "Tie"
        elif player_score > 21:
            winner = "You bust! Dealer"
        elif dealer_score > 21:
            winner = "Dealer bust! You"
        else:
            winner = "You" if player_score > dealer_score else "Dealer"
        return winner

    def update_player_money(self, winner):
        player_won = True
        if winner in ["You bust! Dealer", "Dealer"]:
            player_won = False
        self.player.update_money(player_won)

    def play_again(self):
        prompt = "==> Want to continue playing? (y/n): "
        while True:
            playing_choice = input(prompt).lower()
            if playing_choice in ['y', 'n']:
                break
            print('Invalid Input! Expecting "y" for yes or "n" for no.')
        return playing_choice == 'y'

    def display_welcome_message(self):
        clear_screen()
        print("* WELCOME TO TWENTY ONE *\n")
        self.display_rules()

    def display_rules(self):
        print("... Rules go here ...\n")

    def display_goodbye_message(self):
        print("Thanks for playing Twenty One! Goodbye!")

    def display_result_update_money(self):
        clear_screen()
        print("* RESULTS *")
        winner = self.determine_winner()
        if winner == "Tie":
            print("It's a tie!")
        else:
            print(f"{winner} won!")
            self.update_player_money(winner)
        self.player.display_money_available()
        print(f"\n{self.dealer.reveal_hand()} \n"
                f"Dealers Score: {self.dealer.current_score()}\n")
        print(f"{self.player.display_hand("Your Hand")} \n"
                f"Your Score: {self.player.current_score()}\n")

game = TwentyOneGame()
game.start()
