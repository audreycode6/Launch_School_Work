'''Given a string of words separated by spaces,
write a function that swaps the first and
last letters of every word.

You may assume that every word contains at
least one letter, and that the string will
always contain at least one word. You may 
also assume that each string contains nothing
but words and spaces, and that there are no leading,
trailing, or repeated spaces.
'''

'''p:
in: string -> string of words seperated by spaces
out: return string: swaps the first and last letters of every word.
e: 
    -  swap 1st and last chars of each word
    -may assume that every word contains atleast one letter, 
    and that the string will always contain at least one word. 
    - each string contains nothing but words and spaces, and that there are no leading, trailing, or repeated spaces
i:
    - split the string up by words (delimited by spaces)
?'s:
'''

'''E:
print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True
'''

'''d:
-list to store words in string : .split()
- index accessing to get first and lst char: [0], [-1]
- .join() to join strs in list
'''

'''a:
1. take in a string
2. split string up by words, store in list: .split()
3. new empty list to store swaped char strs
4. loop through words and swap 1st and last char in words
    -append to new list
5. join words in list to one str and return
'''

def swap(string):
    list_words = string.split()
    swapped_list = []

    for word in list_words:
        if len(word) > 1:
            word = word[-1] + word[1:-1]+  word[0]
        swapped_list.append(word)

    return ' '.join(swapped_list)

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True
