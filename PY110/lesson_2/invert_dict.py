'''Given a dictionary where both keys and values are unique, 
invert this dictionary so that its keys become 
values and its values become keys.
'''
'''P:
in: dict: keys and values are uique
out: original dict inverteD: value = key, key = value
e:
i:
?:
'''


def invert_dict(dictionary):
    '''OR for loop way'''
    # new_dict = {}
    # for key, value in dictionary.items():
    #     new_dict[value] = key
    return {value: key for key, value in dictionary.items()}

print(invert_dict({
          'apple': 'fruit',
          'broccoli': 'vegetable',
          'salmon': 'fish',
      }) == {
          'fruit': 'apple',
          'vegetable': 'broccoli',
          'fish': 'salmon',
      })  # True