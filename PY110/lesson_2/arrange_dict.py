'''Given a dictionary, return its keys sorted by the values associated with each key.

'''

'''P:
in: dict
out:list: dict keys sorted by its values
e:
i:
?:
'''

'''e:
['q', 'r', 'p']
'''
'''d:
- .keys()
- .values()
- for key, value in dict
- .sort / sorted()
'''

'''a:
1. take in dict
2. for value in dict:
    -sort acending
3. return list of matching keys of sorted values
'''

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
def order_by_value(my_dict):
    '''reverse original dict so can sort by values and access by key'''
    new_dict = {value: key for key, value in my_dict.items()}

    return [new_dict[num] for num in sorted(new_dict)] # list of sorted (by value) keys

print(order_by_value(my_dict) == keys)  # True

# OR LS WAY
def sort_key(item):
    return item[1] # tuple item(key, value) -> value 

# helpful to visualize sort_key()
for item in my_dict.items():
    print(item[1])# tuple item(key, value) -> value 

def order_by_val(my_dict):
    sorted_item = sorted(my_dict.items(), key=sort_key) # sort the dict items by value  (sort_key)
    
    return [key for key, value in sorted_item]

print(order_by_val(my_dict) == keys)

