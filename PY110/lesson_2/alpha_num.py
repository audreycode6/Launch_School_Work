'''Write a function that takes a list of integers 
between 0 and 19 and returns a list of those 
integers sorted based on the English word 
for each number:
zero, one, two, three, four, five, six, seven, eight,
nine, ten, eleven, twelve, thirteen, fourteen, 
fifteen, sixteen, seventeen, eighteen, nineteen
'''

'''P:
in: list: of ints between 0-19 
out: list: of those ints sorted by their english word
e:
-take in num and sort by its string form
-sort by strings
-return list of ints rearranged by str
-can be any num 0-19 inclusive
i:
?:
do we care about mutating original list?
'''

'''e:
input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(input_list) == expected_result)
# Prints True
'''

'''D:
use dict: key is string of int word and value is int
    -using int as value will make it easier to return(?)
-for loop to loop through elem in list
- sort or sorted, key = str
'''

'''A:
'''
ALPHA_NUM = { 'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six':6,
             'seven': 7, 'eight': 8, 'nine' : 9, 'ten': 10, 'eleven' : 11, 'twelve': 12,
             'thirteen' : 13, 'fourteen': 14, 'fifteen': 15, 'sixteen' : 16, 
             'seventeen': 17, 'eighteen' : 18, 'nineteen' : 19
             }   
NUM_ALPHA = { 0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
             7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
             13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 
             17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
            }


input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
input_list2 = [2, 4, 6, 8, 10]
expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

'''My way:  use 2 dicts: 1. to find matching word form for num and
 2. viceversa when converting sorted word_form_num to number form'''
def alphabetic_number_sort(input_list):
    # convert ints to matching string list and sort by string
    string_list = sorted([NUM_ALPHA.get(elem) for elem in input_list])

    # convert string to matching int
    int_sorted_by_string = [ALPHA_NUM.get(elem) for elem in string_list]

    return int_sorted_by_string 

print(alphabetic_number_sort(input_list2)) # [8, 4, 6, 10, 2]
print(alphabetic_number_sort(input_list) == expected_result)


NUM_STRS = [ 'zero', 'one', 'two', 'three', 'four', 'five', 'six',
            'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
            'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
            'eighteen', 'nineteen']

'''LS way: NUM_STRS: use constant_list of string of num in word form; 
index == num; for elem in input_list find matching word form and add to list
sort by str '''
def alphabetic_number_sort2(input_list):
    # list of matching string for num in input, sorted by string
    foo = sorted([NUM_STRS[num] for num in input_list])

    # list of index (matching int) of string in foo
    bar = [NUM_STRS.index(string) for string in foo]
    return bar

print(alphabetic_number_sort2(input_list2)) # [8, 4, 6, 10, 2]
print(alphabetic_number_sort2(input_list) == expected_result)
