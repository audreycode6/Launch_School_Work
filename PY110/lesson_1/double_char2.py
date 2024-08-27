'''Write a function that takes a string, doubles every 
consonant in the string, and returns the result as a 
new string. The function should not double vowels 
('a','e','i','o','u'), digits, punctuation, or whitespace.

You may assume that only ASCII characters will be included in the argument.'''

'''P:
in: string
out: new string: double every consonany in stirng
e:
- only ascii chars included in str
- do not double vowels, digits, punctutaution or whitespace
-return new string with consonat chars doubled
i:
-case insenstive
-empty str == empty str
-no consonant reutrn str unchanged
?'s:
'''

'''a:
1. take in a string
2. check each char if consonant and append double char if consonant 
or original char if not consonant
    -maybe ternary
    -double consonants, else remain same
3. return final string with consonants doubled
'''

vowels = ['a', 'e', 'i', 'o', 'u']
def double_consonants(string):
    new_str = ''
    for char in string:
        if char not in vowels and char.isalpha() == True:
            char = char * 2
        new_str += char

    return new_str

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")