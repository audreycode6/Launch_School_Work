'''Modify the word_sizes function from the previous 
exercise to exclude non-letters when determining 
word size. For instance, the word size of "it's"
 is 3, not 4.'''

'''a:
1. take in string
2. new string with only alpha chars
3. store clean strings (delimited by whiutespace) in list 
4. loop through words and count length
    - if length is less than 1 dont do loop
    - check if key exists, if it does +=1 else  (dict.setdefault(length, 0))
    - add length of string as key in dict
5. return dict
'''

''' helper func: return new string with only alpha chars
and spaces remaining '''
def only_alpha(string):
    only_alpha = ''
    for char in string:
        if char.isalpha() or char.isspace():
            only_alpha += char
    
    return only_alpha

''' main entry point: take in string and return dict:
 keys -> length of words (alpha chars only) in string 
 and value -> # of words that length '''
def word_sizes(string):
    list_words = only_alpha(string).split()

    word_length_count = {}
    for word in list_words:
        length = len(word)

        if length > 0:
            word_length_count.setdefault(length, 0)
            word_length_count[length] += 1

    return word_length_count


# All of these examples should print True
string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})
string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})
string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})
string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})
print(word_sizes('') == {})