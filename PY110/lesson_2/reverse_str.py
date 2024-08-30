'''You have a function that is supposed to 
reverse a string passed as an argument.
However, it's not producing the expected output.
Explain the bug, and provide a solution.
'''

'''original to debug:
def reverse_string(string):
    for char in string:
        string = char + string # currently adds each char to original string 
        # so we get reversed str concatenated with orignal str
        # string is the orignal input so we dont want to use 
        # that variable when creating the new str
        print(string)

    return string

print(reverse_string("hello")) #== "olleh") -> ollehhello
'''

'''solution'''
def reverse_string(string):
    revers_str = ''
    for char in string:
        revers_str = char + revers_str 
    
    return revers_str # OR string[::-1]

print(reverse_string("hello")== "olleh") # True
