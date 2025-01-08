'''Implement a Wallet class that represents a wallet
with a certain amount of money. You want to be able 
to combine (add) two wallets together to get a new wallet
with the combined total amount from both wallets.'''

'''SOLUTION STEPS:
-create Wallet class
- init takes in money arg
- allow wallets to be combinned
    - define magic method to make arith + operator to work
        -__add__(self, other)
'''

class Wallet:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        if isinstance(other, Wallet):
            # returns a new Wallet object from result of adding both wallet amounts
            return Wallet(self.amount + other.amount) 
        return NotImplemented  

wallet1 = Wallet(50)
wallet2 = Wallet(30)
merged_wallet = wallet1 + wallet2
print(merged_wallet.amount == 80)       # True