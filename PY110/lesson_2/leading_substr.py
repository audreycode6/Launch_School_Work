'''Write a function that takes a string argument and
returns a list of substrings of that string. Each 
substring should begin with the first letter of the word,
and the list should be ordered from shortest to longest.
'''

'''P:
in:string
out:list: elements are substrings of input string
e:
- each substr should begin with the first letter of the word
-list ordered by shorted to longest
i:
- substr = increment string by one of its chars until spelling out original str
- list = [first_char, 1st_2nd_char, 123char, ... full str]
?: empty str input?
'''

'''e:
# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])
'''

'''d:
for char in str: make list of char
chars increment by 1 // maybe slice? [:1] 1 increments until len of str
'''

'''A:
1. take in string
2. make new list:
    - for len of str: add new str 
     -start with 1st char and increment 1 more char until spelling out orignal str
      
3. return list of substrs '''

def leading_substrings(string):
    # OR
    '''for loop way'''
    list_of_substrs = []
    for num in range(1,len(string)+1):
        foo = string[:num]
        list_of_substrs.append(foo)
    print(list_of_substrs)

    return [string[:num] for num in range(1, len(string)+1)] # TODO: list of substrings

print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])