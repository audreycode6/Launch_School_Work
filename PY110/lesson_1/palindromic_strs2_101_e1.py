'''Write another function that returns True if the
string passed as an argument is a palindrome, or
False otherwise. This time, however, your function
should be case-insensitive, and should ignore all
non-alphanumeric characters. If you wish, you may
simplify things by calling the is_palindrome
function you wrote in the previous exercise.'''

'''a:
    1. take in str input
    2. loop through str and if char.isalphanumeric() add to new string
    3. return eval: string.lower() == new_string.lower()
      '''

def is_real_palindrome(string):
    al_num_str = ''
    for char in string:
        if char.isalnum() and char.isascii():
            al_num_str += char
    al_num_str = al_num_str.casefold() 
    return al_num_str == al_num_str[::-1]
        
print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True
print(is_real_palindrome('Madam') == True)           # True
print(is_real_palindrome("Madam, I'm Adam") == True) # True
