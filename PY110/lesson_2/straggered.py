'''Write a function that takes a string as an argument 
and returns that string with a staggered capitalization 
scheme. Every other character, starting from the first, 
should be capitalized and should be followed by a 
lowercase or non-alphabetic character. Non-alphabetic 
characters should not be changed, but should be counted 
as characters for determining when to switch 
between upper and lower case.
'''

'''P:
in: string
out: string with a staggered capitalization scheme
    - Every other character, starting from the first, 
        should be capitalized and should be followed by a 
        lowercase or non-alphabetic character
    - Non-alphabetic characters should not be changed, 
        but should be counted 
        as characters for determining when to switch 
        between upper and lower case.
e:
- if non alpha char do nothing
- if alpha char either upper or lower
- first char is upper a
i:
?
'''

'''d:
maybe coerse to all lower at first
add to new string
for char in string
maybe upper = T and if index odd lower (upper = F(?))/ if index even upper = T
if char.isalpha() == False add element unchanged to new str
else if upper = T and char.isalpha() char.upper()
'''

'''A:
1. take in string
2. intialize empty str
3. for idx, char in numerate(string):
    if char.isalpha == True and idx % 2 == 0:
        char = char.upper
    empty_str += char
'''

def staggered_case(string):
    new_str = ''
    for idx, char in enumerate(string.lower()):
        if idx % 2 == 0:
            char = char.upper()
        new_str += char

    return new_str 

string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True