'''Write a function that takes a string as an argument
and returns True if all parentheses in the string are 
properly balanced, False otherwise. To be properly 
balanced, parentheses must occur in matching 
'(' and ')' pairs.
Note that balanced pairs must start with a (, not a ).
'''
'''P:
in: string
out: boolean: T or F: True if all parentheses in the string are 
properly balanced; False otherwise
e:
- To be properly balanced, parentheses must occur in matching '(' and ')' pairs
i:
- equal '(' ')' count != they are balanced
?'s:
'''

'''e:
'''

'''d:
left = '('
right = ')'
if left.count == right.count then T, else F , jjk
maybe for each '(' or ')' append to string and then check string if they close
'''

'''a:
1. take in str
2. new str with only parentheses 
3. check len(new_str) // 2 == 0:
    -T continue to check if balanced
    - else return F
4. Check if new_str has balanced parenth
    ...
5. Return boolean
'''
PARENTHESES = ['(', ')']

'''helper func: return string of only parentheses from original str'''
def parenthese_string(string):
    parentheses_str = ''
    for char in string:
        if char in PARENTHESES:
            parentheses_str += char
    return parentheses_str

def is_balanced(string):
    '''new str of just parentheses in string'''
    paren_str = parenthese_string(string)

    if paren_str:
        '''check if parentheses balanced'''
        if (
            (paren_str[0] != '(' or paren_str[-1] != ')') or 
            (paren_str.count(PARENTHESES[0]) != paren_str.count(PARENTHESES[1]))
            ):
            return False

    return True

print(is_balanced("(What )is((())) this?)") == False)
print(is_balanced("What (is))) this?") == False)
print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True 
