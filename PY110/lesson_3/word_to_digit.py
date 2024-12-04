'''Write a function that takes a string as an argument 
and returns that string with every occurrence of a
"number word" -- 'zero', 'one', 'two', 'three',
'four', 'five', 'six', 'seven', 'eight', 'nine' -- 
converted to its corresponding digit character.

You may assume that the string does not contain any punctuation.
'''

'''P:
in:string
ouT: string with every occurence of number word ( 'zero', 'one', 'two', 'three',
'four', 'five', 'six', 'seven', 'eight', 'nine')) converted to its corresponding digit char
e:
-string doesnt contain any puncutation
I:
?:
'''

def word_to_digit(string):
    string_nums = ['zero', 'one', 'two', 'three',
                    'four', 'five', 'six', 'seven',
                        'eight', 'nine']
    words = string.split()
    for idx, word in enumerate(words):
        if word in string_nums:
            matching_num = string_nums.index(word)
            words[idx] = str(matching_num)

    return ' '.join(words)

message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True