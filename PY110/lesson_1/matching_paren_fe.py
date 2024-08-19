'''Write a function that takes a string as an argument
and returns True if all parentheses in the string are 
properly balanced, False otherwise. To be properly 
balanced, parentheses must occur in matching 
'(' and ')' pairs.
Note that balanced pairs must start with a (, not a ).
'''

'''Further Exploration
There are a few other characters that should be matching as well. 
Square brackets and curly brackets normally come in pairs. 
Quotation marks(single and double) also typically come in pairs and 
should be balanced. Can you expand this function to take 
into account those characters?'''

PARENTHESES = ['(', ')']
SQUARE_BRACKETS = ['[', ']']
CURLY_BRACKETS = ['{', '}']
BEGINNING_CHARS = ['[', '(', '{']
ENDING_CHARS = [']', ')', '}']

'''helper func: return string of only parentheses from original str'''
def isolate_chars(string):
    complete_chars = ''
    for char in string:
        if (
        (char in PARENTHESES) or 
        (char in SQUARE_BRACKETS) or 
        (char in CURLY_BRACKETS)
        ):
            complete_chars += char

    return complete_chars 

def is_balanced(string):
    '''new str of just parentheses in string'''
    paren_square_curly = isolate_chars(string)
     
    if paren_square_curly: # if not empty str
        # check 1st and last char 
        if ((paren_square_curly[0] not in BEGINNING_CHARS) or
        (paren_square_curly[-1] not in ENDING_CHARS)): 
            return False
        # check count of chars: ( & ), [ & ], { & } are equal
        if ((paren_square_curly.count(PARENTHESES[0]) != 
            paren_square_curly.count(PARENTHESES[1])) or 
            (paren_square_curly.count(SQUARE_BRACKETS[0]) !=
            paren_square_curly.count(SQUARE_BRACKETS[1])) or
            (paren_square_curly.count(CURLY_BRACKETS[0]) != 
            paren_square_curly.count(CURLY_BRACKETS[1]))): 
            return False
    return True

print(is_balanced("{What }is{{{}}} this?}") == False) # True
print(is_balanced("What [is]]] this?") == False)    # True
print(is_balanced("What {is} this?") == True)        # True
print(is_balanced("What is] this?") == False)        # True
print(is_balanced("What [is this?") == False)        # True
print(is_balanced("[{What} [is this]]?") == True)    # True
print(is_balanced("[[What]] {is this}}?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced("]Hey![") == False)                # True
print(is_balanced("What ({is})) up(") == False)      # True 

# print(is_balanced("What [is] this?") == True)
# print(is_balanced("What is} this?") == False)
# print(is_balanced("What {is this?") == False)
# print(is_balanced("({What} (is this))?") == True)
# print(is_balanced("((What)) (is this))?") == False)
# print(is_balanced("Hey!") == True)
# print(is_balanced(")Hey!(") == False)
# print(is_balanced("What ({is]}) up(") == False)
