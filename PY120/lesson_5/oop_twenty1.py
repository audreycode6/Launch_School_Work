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
        cards_dealt = []
        for _ in range(number_of_cards):
            card = random.choice(self.deck)
            self.deck.remove(card)
            cards_dealt.append(card)
        return cards_dealt

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

    def display_hand(self):
        hand_size = len(self.hand)
        player = "Your" if isinstance(self, Player) else "Dealer's"
        if hand_size == 2:
            return f"{player} Hand: {' and '.join(self.hand)}"

        last_card = self.hand[-1]
        all_but_last_card = self.hand[:-1]
        return (f"{player} Hand:"
                 f" {", ".join(all_but_last_card)}, and {last_card}")

    def stay(self):
        pass

    def has_busted(self):
        return self.get_current_score() > TwentyOneGame.MAX_SCORE

    def evaluate_ace_cards(self, ace_cards):
        ace_score = len(ace_cards) * 1
        for _ in ace_cards:
            while (self.score + ace_score) <= 11:
                # 11 is the max score before an Ace becomes 1 instead of 11
                ace_score += 10

        return ace_score

    def get_ace_and_non_ace_cards(self):
        ace_cards = [card
                    for card in self.hand
                    if card.split()[0] == "Ace"]
        not_ace_cards = [card
                        for card in self.hand
                        if card.split()[0] != "Ace"]
        return ace_cards, not_ace_cards

    def get_current_score(self):
        self.score = 0
        ace_cards, not_ace_cards = self.get_ace_and_non_ace_cards()
        if not_ace_cards: # eval non ace cards
            for card in not_ace_cards:
                cards = card.split()
                rank = cards[0]
                if rank in ["Jack", 'Queen', "King"]:
                    value = 10
                else:
                    value = int(rank)
                self.score += value

        if ace_cards: # eval ace cards
            ace_score = self.evaluate_ace_cards(ace_cards)
            self.score += ace_score

        return self.score

class Player(Participant):
    MAX_MONEY = 10
    STARTING_BALANCE = 5

    def __init__(self):
        super().__init__()
        self.betting_balance = Player.STARTING_BALANCE

    def stay(self):
        clear_screen()
        print("* You chose to stay! *")
        print("\n... Dealer's turn ...\n")

    def update_money(self, player_won):
        if player_won:
            self.betting_balance += 1
            print("+ You earned another dollar! +")
        else:
            self.betting_balance -= 1
            print("- You lost a dollar! -")

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

    def display_hidden_hand(self):
        one_card = self.hand[0]
        return f"Dealer's Hand: {one_card} and unknown card"

    def reveal_hand(self):
        return super().display_hand()

class TwentyOneGame:
    MAX_SCORE = 21

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
            self.display_and_update_results()
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
        if not self.player.has_busted():
            self.dealer_turn()

    def is_match_over(self):
        return self.player.betting_balance in [0, Player.MAX_MONEY]

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
            if self.player.betting_balance == Player.MAX_MONEY:
                print("You're too good at this game!"
                      " Take your money and go ...")
            else:
                print("You're broke! No money, no playing ...")

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
        error_prompt = (
            "\n!!   Invalid Input: Enter 'h' to hit &"
                    " add another card to your deck"
                    " or 's' to stay & keep the hand"
                    " you have   !!\n")
        prompt = "\n==> Would you like to hit or stay? (h/s): "

        while True:
            self.show_cards()
            print(f"Your Score: {self.player.get_current_score()}")

            while True:
                hit_or_stay = input(prompt).strip().lower()
                if hit_or_stay in ['h', 's']:
                    break
                print(error_prompt)

            if hit_or_stay == 's':
                self.player.stay()
                break

            self.player.hit(self.deck)
            if self.player.has_busted():
                break

    def dealer_turn(self):
        while self.dealer.get_current_score() < 17:
            # dealer hits until >= 17
            self.dealer.hit(self.deck)
        if not self.dealer.has_busted():
            self.dealer.stay()
        input("\n==> Press Enter to see the results: ")
        clear_screen()

    def determine_winner_and_update_money(self):
        player_score = self.player.get_current_score()
        dealer_score = self.dealer.get_current_score()

        # determine winner
        if player_score == dealer_score: # tie
            return "It's a tie"
        if player_score > TwentyOneGame.MAX_SCORE: # player bust
            winning_message = "Dealer wins! You bust!"
        elif dealer_score > TwentyOneGame.MAX_SCORE: # dealer bust
            winning_message = "You win! Dealer bust!"
        else: # both scores in range (<=21)
            winning_message = ("You win!" if player_score > dealer_score
                                else "Dealer wins!")

        # update player money (+/-)
        player_won = False
        if winning_message.split()[0].startswith("You"):
            player_won = True
        self.player.update_money(player_won)

        return winning_message

    def play_again(self):
        continue_playing = ["y", "yes"]
        prompt = "==> Want to continue playing? (y/n): "
        while True:
            playing_choice = input(prompt).lower().strip()
            if playing_choice in ["yes", "y", "no", "n"]:
                break
            print('Invalid Input! Expecting "y" / "yes" or "n" / "no".')
        return playing_choice in continue_playing

    def display_welcome_message(self):
        clear_screen()
        print("* WELCOME TO TWENTY ONE *\n")
        self.display_rules()

    def display_rules(self):
        print("RULES:")
        print("You're playing against the dealer.\n"
        "The goal is to get as close to 21 without going over.\n"
        "\nYou start with 2 cards and are asked if you want to:\n"
        "- Hit: add another card to your hand * OR *\n"
        "- Stay: keep the current hand you have\n")
        print("\nCARD RANKING:\n"
        "- Ace: 1 or 11 (whatever gets you closest to 21)\n"
        "- Jack, Queen, King: 10\n"
        "- all others are face value: (2-10)\n")
        input("==> Press Enter to continue to the game: ")
        clear_screen()

    def display_goodbye_message(self):
        print("\nThanks for playing Twenty One! Goodbye!")

    def display_and_update_results(self):
        clear_screen()
        print("* RESULTS *")
        winning_message = self.determine_winner_and_update_money()
        print(winning_message)
        self.player.display_money_available()
        print(f"\n{self.dealer.reveal_hand()} \n"
                f"Dealer's Score: {self.dealer.get_current_score()}\n")
        print(f"{self.player.display_hand()} \n"
                f"Your Score: {self.player.get_current_score()}\n")

game = TwentyOneGame()
game.start()