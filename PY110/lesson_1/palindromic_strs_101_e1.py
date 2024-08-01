'''Write a function that returns True if the string passed
as an argument is a palindrome, False otherwise.
A palindrome reads the same forwards and backwards.
For this problem, the case matters and all characters matter.'''

'''a:
    1. take in string input
    2. new string: reversed_str, reverse original str 
    3. return bool of eval: orignal str == reversed_str
'''

def is_palindrome(string):
    return string[::-1] == string

# All of these examples print True:
print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)
print(is_palindrome('Madam') == False)
print(is_palindrome("madam i'm adam") == False)