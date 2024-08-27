'''Write a function that takes a string consisting 
of zero or more space-separated words and returns a
 dictionary that shows the number of words of different sizes.
Words consist of any sequence of non-space characters.
'''
'''a:
    1. take in string
    2. seperate string by words (whitespace delimiter)
    3. intitalize empty dict (to add k: lenghts, v: # of words)
    3. loop through words and find len(word) add as key in dict
        - if key exists value += 1
        - else value = 1
    4. return dict 
    '''

def word_sizes(string):
    list_words = string.split(' ')
    word_length_count = {}

    for word in list_words:
        length = len(word)

        if length > 0:
            word_length_count.setdefault(length, 0)
            word_length_count[length] += 1

    return word_length_count

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})
string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})
string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})
string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})
print(word_sizes('') == {})