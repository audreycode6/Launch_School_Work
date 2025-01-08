
class House:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    def __lt__(self, other):   # NEW
        if not isinstance(other, House):
            return NotImplemented
        return self.price < other.price
    '''OR this works too:
        if isinstance(other, House):
            return self.price < other.price
        return NotImplemented
    '''
    
    def __gt__(self, other):  # NEW
        if not isinstance(other, House):
            return NotImplemented
        return self.price > other.price

home1 = House(100000)
home2 = House(150000)
if home1 < home2: # new
    print("Home 1 is cheaper")
if home2 > home1: # new
    print("Home 2 is more expensive")

'''EXPECTED OUTPUT:
Home 1 is cheaper
Home 2 is more expensive
'''
'''TODO: Modify the House class so the above program work as shown.
-use the <, > magic methods: __lt__, __gt__ 
    so program can accurately read comparison operators
'''