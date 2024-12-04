'''try both ways: solve only in a single for loop 
    VS solve by iterating though dict after creation 
    and changing values based on conditions'''

target_letters = ['a', 'b', 'c', 'd', 'e']
characters = ['a', 'b', 'b', 'd', 'f', 'f', 'z', 'z', 'z']
expected_result = {
    'a': { 'present': True, 'count': 1 },
    'b': { 'present': True, 'count': 2 },
    'c': { 'present': False, 'count': 0 },
    'd': { 'present': True, 'count': 1 },
    'e': { 'present': False, 'count': 0 },
}


''' solving using for loop to create dictionary'''
my_dict = {}
for char in target_letters:
        my_dict[char] = {'present' : (char in characters),
                      'count': characters.count(char)}

print(expected_result == my_dict) # True


''' OR solving using dict comprehension'''
my_comp = {char : {'present' : (char in characters),
                    'count': characters.count(char)} 
                    for char in target_letters}

print(my_comp == expected_result) # True


''' OR solving by creating dict first and then iterating
through it to update values for 'present' 
and 'count' '''
char_dict = {char : {'present' : False, 'count' : 0 } 
             for char in target_letters}

for key, value in char_dict.items():
    if key in characters:
        value['present'] = True
    value['count'] = characters.count(key)
    
print(char_dict == expected_result) # True