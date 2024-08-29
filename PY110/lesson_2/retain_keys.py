'''Given a dictionary and a list of keys, 
produce a new dictionary that only contains
the key/value pairs for the specified keys.
'''

'''P:
in:2 args: dict, list of dict keys
out: new dict only containing key/value pairs of sp[ecified keys]
e:
- make new dict of k-v pairs that match keys in lst
i:
?:
'''

'''d:
- dict.items()
new_dict'''

def keep_keys(dicty, lst):
    '''for loop way'''
    # new_dict = {}
    # for key, value in dicty.items():
    #     if key in lst:
    #         new_dict[key] = value
        
    '''OR with .items()'''
    # {key: value for key, value in dicty.items() if key in lst}

    return {key: dicty[key] 
            for key in dicty 
            if key in lst}

input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True