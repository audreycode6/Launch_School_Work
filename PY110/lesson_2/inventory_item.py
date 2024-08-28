'''Write a function that takes two arguments,
an inventory item ID and a list of transactions,
and returns a list containing only the 
transactions for the specified inventory item.'''

'''P:
in: 2 args: int, list(of dicts ->transactions)
out: list: containing transactions for specified inventory item
e:
- 1st arg = 'id' value
    - transactions search elements if element['id'] == 1st arg then list index

- new list of elements with matching id

i:
- multiple id's with same value
?:
'''
'''a:
1. take in 2 args: id_int, list_transaction
2. loop through elements in list -- enumerate()
    - if element['id] is match store index in new list (whole element at that index)'''

transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]
def transactions_for(id_int, lst):
    return [element for element in lst if element['id'] == id_int]

print(transactions_for(101, transactions) ==
      [
          {"id": 101, "movement": "in",  "quantity":  5},
          {"id": 101, "movement": "in",  "quantity": 12},
          {"id": 101, "movement": "out", "quantity": 18},
      ]) # True