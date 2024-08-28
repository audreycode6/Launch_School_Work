'''Building on the previous exercise, write a function that 
returns True or False based on whether or not an inventory 
item (an ID number) is available. As before, the function 
takes two arguments: an item ID and a list of transactions. 
The function should return True only if the sum of the 
quantity values of the item's transactions is greater than 
zero. Notice that there is a movement property in each 
transaction object. A movement value of 'out' will 
decrease the item's quantity.

You may (and should) use the transactions_for
 function from the previous exercise.
'''

'''P:
in: 2 args: id_int , lst_transaction
out: boolean: T or F ( based on whether or not an inventory 
item (an ID number) is available.)
E:
-True only if the sum of the quantity values of 
    the item's transactions is greater than zero
- there is a movement property in each 
    transaction object. A movement value of 'out' will 
    decrease the item's quantity 
- use past funcy
- 
i:
?:
'''

'''d:
in_sum and out_sum variable: grab from dict object ['movement']
    -insum = sum[['quanity'] for 'in' in ['movement']] -OR for loop and 2 lists depending if 'in' or 'out'
    -outsum = sum[['quanity'] for 'out' in ['movement']]
-transaction var = insum - outsum
    - if transaction > 0: return T -> else F
'''

'''A:
1. take in id and list of transactions
2. call func: transactions_for(id, lst) to access only id elemets u care about
    for each element:
        -check '['movement'] : is 'in' or 'out'
        -check quantity:
        - if 'in' add to in_sum
        -if 'out' add to out_sum
    - calc transactions_total = in - out
        - if transaction > 0 return T, else F
              '''

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

'''helper func return list of all dicts with matching id'''
def transactions_for(id_int, lst):
    return [element for element in lst if element['id'] == id_int]

'''return boolean:  for id_int's id in lst, 
if total quantity's value for 'in' movement is 
greater than total quantity's for 'out' movement return True, else False  '''
def is_item_available(id_int, lst):
    id_elements = transactions_for(id_int, lst)

    '''LS way: 1 int for quantity total instead on my in_sum and out_sum lists'''
    # quantity_total = 0
    # for element in id_elements:
    #     quantity = element['quantity']
    #     if element['movement'] == 'in':
    #         quantity_total += quantity
    #     else:
    #         quantity_total -= quantity
    # return quantity_total > 0

    '''my way: list comp way'''
    # in_sum = [element['quantity'] for element in id_elements if element['movement'] == 'in']
    # out_sum = [element['quantity'] for element in id_elements if element['movement'] == 'out']

    '''my way: for loop way'''
    in_sum = []
    out_sum = []
    for element in id_elements:
        quantity = element['quantity']
        if element['movement'] == 'in':
            in_sum.append(quantity)
        else:
            out_sum.append(quantity)

    return (sum(in_sum) - sum(out_sum)) > 0

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True