'''Modify the function from the previous exercise so it 
ignores non-alphabetic characters when determining 
whether it should uppercase or lowercase each letter. 
The non-alphabetic characters should still be included 
in the return value; they just don't count when 
toggling the desired case.
'''

'''P:
in: string
ouT: staggered string: 
    -ignores non-alphabetic characters when determining 
        whether it should uppercase or lowercase each letter. 
        The non-alphabetic characters should still be included 
        in the return value; they just don't count when 
        toggling the desired case.
e:
- index will not be the determining factor for upper/lower
-modify previous func
-
I:
?:
'''

'''d:
-maybe use variable to alternate between upper. T or F'''

'''A:
1. take in string
2. intitalize variable to track upper: upper = True
2. for char in string.lower():
    -if char.islpaha():
        -if track_upper = True:
            char = char.upper()
        -else:
            track_upper = False
    new_str += char
'''

'''my way: less concise than LS way'''
# def staggered_case(string):
#     stagger_str = ''
#     make_upper = True
    
#     for char in string.lower():
#         if char.isalpha() and make_upper:
#             stagger_str += char.upper()
#             make_upper = False
#             continue
#         stagger_str += char
#         if char.isalpha():
#             make_upper = True

#     return stagger_str 

'''LS Way: 
- ternary expression for if char.isalpha() (lower or upper char)
- not to get inverse of make_upper
'''
def staggered_case(string):
    stagger_str = ''
    make_upper = True
    
    for char in string:
        if char.isalpha():
            stagger_str += char.upper() if make_upper else char.lower()
            make_upper = not make_upper  
        else:
            stagger_str += char
    return stagger_str 


string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True