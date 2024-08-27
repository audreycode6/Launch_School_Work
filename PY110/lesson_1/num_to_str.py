'''In this exercise and the next, you're going to
reverse previous convert_string...() functions.

Write a function that converts a non-negative integer
 value (e.g., 0, 1, 2, 3, and so on) to the string
representation of that integer.

You may not use any of the standard conversion
functions available in Python,(str). 
Your function should do this the old-fashioned way
and construct the string by analyzing and 
manipulating the number.'''

'''a:
1. take in an int
2. convert num to str
    ... string interpolation str_int = f'{}'
3. return str_int

'''

def integer_to_string(integer):
    int_str = ''
    # follows 0 index so using indexing with remainder give matching digit char
    DIGIT_CHARS = ['0','1','2','3','4','5','6','7','8','9']

    while integer > 0:
        # remainder = 1's place of integer, 
        # integer decreases 1's place each loop
        integer, remainder = divmod(integer, 10)

        # add each remainder to front bc we continue 
        # to get the following place value of integer
        int_str = DIGIT_CHARS[remainder] + int_str

    return int_str or '0' # if 0 input int_str = 0 which is falsy

# OR THIS IS done implicitely
    # def integer_to_string(integer):
    #     return f'{integer}'

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(31) == "31")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True