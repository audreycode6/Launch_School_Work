'''Write a function that takes a string, doubles every 
character in the string, then returns the result as a new string.'''

'''P:
in: string
out: new string with each char from original str doubled
e:
-double each char from original str
-new str
I:
?'s:
'''

'''e:
print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True
'''

'''d:
for loop original str
new_char = char * 2
empty str += new_char

or listcomprehension and then .join()
'''

'''a:
1. take in a str
2. make empty str to create new list
3. loop through original str
    - for each char: char * 2
    -append new str to new str
4. return new str
'''

def repeater(string):
    new_list = [char * 2 for char in string]
    return ''.join(new_list)

# OR FOR LOOP AND APPEND TO NEWSTR
    # new_str = ''
    # for char in string:
    #     new_char = char * 2
    #     new_str += new_char
    # return new_str

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True
