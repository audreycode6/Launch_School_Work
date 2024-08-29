'''Write a function that takes a string as an argument 
and returns a list that contains every word from 
the string, with each word followed by a space and 
the word's length. If the argument is an empty string
 or if no argument is passed, the function should 
 return an empty list.

You may assume that every pair of words in the 
string will be separated by a single space.'''


'''P:
in: string
out: list: every word from string
    - each word followed by a space and the word's length.
e:
- if empty arg return empty list
- every pair of words in the string will be separated by a single space
i:
?:
'''

'''d:
len()
' '.split() 
+= to add len to string
'''

'''a:
1. take in string
2. split string into list of words
3. for word in str_lst:
    - find len + and add to end of str + space
4. return final list of words: 
'''

'''MY WAY: for loop'''
# def word_lengths(string=''):
#     # ensure not empty arg
#     if len(string) < 1:
#         return []
    
#     # convert str to list of words
#     str_lst = string.split(' ')

#     # loop through words and find len + update str
#     for idx, string in enumerate(str_lst):
#         str_lst[idx] = f'{string} {len(string)}'

#     return str_lst 

''' LS WAY: use lst comp -- more concise'''
def word_lengths(string=''):
    # ensure not empty arg
    if not string: # cleaner then checking for len(string)
        return []
    
    return [f'{word} {len(word)}'
            for word in string.split(' ')]

# All of these examples should print True
words = 'cow sheep chicken'
expected_result = ['cow 3', 'sheep 5', 'chicken 7']
print(word_lengths(words) == expected_result)        # True

words = 'baseball hot dogs and apple pie'
expected_result = ['baseball 8', 'hot 3', 'dogs 4',
                   'and 3', 'apple 5', 'pie 3']
print(word_lengths(words) == expected_result)        # True

words = "It ain't easy, is it?"
expected_result = ['It 2', "ain't 5", 'easy, 5',
                   'is 2', 'it? 3']
print(word_lengths(words) == expected_result)        # True

big_word = 'Supercalifragilisticexpialidocious'
print(word_lengths(big_word) == [f'{big_word} 34'])  # True

print(word_lengths('') == [])                        # True
print(word_lengths() == [])                          # True