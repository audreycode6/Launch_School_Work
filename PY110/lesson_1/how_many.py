'''Write a function that counts the number of
occurrences of each element in a given list. 
Once counted, print each element alongside the 
number of occurrences. Consider the words case 
sensitive e.g. ("suv" != "SUV").
'''
'''Further:Try to solve the problem when words are case insensitive,
 e.g. "suv" and "SUV" represent the same vehicle type.
'''

'''a:
1. take in list
2. coerce list to set to store unique elements
3. nested loop: for element in set: -> for element in original list: 
    - count element in original list if mathcing element ibn set
    - print f string to output: 'element => #'
'''

'''case sensitive'''
def count_occurrences(my_list):
    for element in set(my_list):
        print(f'{element} => {my_list.count(element)}')

'''case insensitive'''
def count_occurrences2(my_list):
    case_insensitive = [element.casefold() for element in my_list]
    
    for element in set(case_insensitive):
        print(f'{element} => {case_insensitive.count(element)}')
        
# TEST
vehicles2 = ['CAR', 'car', 'truck', 'cAr', 'Suv', 'truck',
            'motorCYCLE', 'motorcycle', 'car', 'truck']
count_occurrences(vehicles2)
print() 
count_occurrences2(vehicles2)
