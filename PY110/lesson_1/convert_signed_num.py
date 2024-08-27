''' extend previous function convert_string_num
to work with signed numbers.

Write a function that takes a string of digits and 
returns the appropriate number as an integer. The 
string may have a leading + or - sign; if the first 
character is a +, your function should return a positive 
number; if it is a -, your function should return a 
negative number. If there is no sign, return a positive number.

You may assume the string will always contain a valid number.

You may not use any of the standard conversion functions 
available in Python, such as int. You may, however, use 
the string_to_integer function from the previous exercise.'''


'''a:
1. take in string 
2. check first element in str: [0] if == + or == - or in digits
    - append - to front of final if -
    -if not in DIGITS pop so we only keep digits in str when checking
3. pass to string to function to return num
'''

DIGITS = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

'''main entry point: check what first char is (+, - , #),
if has a sign to start remove, pass integer to helper func,
if negative sign convert final int to negative value '''
def string_to_signed_integer(integer, DIGITS):
    # check first_char
    negative = False
    first_char = integer[0]
    if first_char in DIGITS:
        pass
    else:
        if first_char == '-':
            negative = True
        integer = integer[1:]

    final_int = string_to_integer(integer, DIGITS)

    # convert final to negative
    if negative:
        final_int = final_int - (2 * final_int)
    return final_int

'''helper func: add integer to matching char in string to list,
convert to complete int: multiple each digit to be expanded form,
add all place value digits together'''
def string_to_integer(integer, DIGITS):
    # char to int -> add to list
    num_list = []
    for digit in integer:
        num = DIGITS.get(digit)
        num_list.append(num)

    # digits from list to expanded form -> standard form
    num_list.reverse()
    number = 0
    for index, num in (enumerate(num_list)):
        if index != 0:
            num = num * (10**index)
        number += num
    final_int = number

    return final_int

print(string_to_signed_integer("4321", DIGITS) == 4321)  # True
print(string_to_signed_integer("-570", DIGITS) == -570)  # True
print(string_to_signed_integer("+100", DIGITS) == 100)  # True