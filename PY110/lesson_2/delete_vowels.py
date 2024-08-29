'''Write a function that takes a list of strings 
and returns a list of the same string values, 
but with all vowels (a, e, i, o, u) removed.
'''

'''P:
in:  list of strings
out: list of same strings but with vowels removed
e:
i:
?:
'''

'''d:
new string = ''
for char in string:
    if char not in vowels -> add to new_string
'''
VOWELS = 'aeiou'

'''helped func to remove vowels from string'''
def new_string(string):
    new_str = [char for char in string 
     if char.lower() not in VOWELS ]
    
    return ''.join(new_str)

def remove_vowels(lst):
    '''list comp way'''
    return [new_string(string) for string in lst]

''' OR 1 func/nested for loop way'''
# def remove_vowels(lst):
#     new_list = []
#     for string in lst:
#         new_str = ''
#         for char in string:
#             if char.lower() not in VOWELS:
#                 new_str += char
#         new_list.append(new_str)

#     return new_list

# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True