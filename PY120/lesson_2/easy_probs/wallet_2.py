'''Using the code from the previous exercise,
modify the code so that when we print the merged_wallet
we receive a message Wallet with $80.'''


class Wallet:
    def __init__(self, amount):
        self.amount = amount
    
    def __str__(self): # NEW
        return f"Wallet with ${self.amount}."

    def __add__(self, other):
        if isinstance(other, Wallet):
            return Wallet(self.amount + other.amount) 
        return NotImplemented  

wallet1 = Wallet(50)
wallet2 = Wallet(30)
merged_wallet = wallet1 + wallet2
print(merged_wallet)          # Wallet with $80.
print(wallet1)