'''Write a function that takes a string of digits and
 returns the appropriate number as an integer. You may 
 not use any of the standard conversion functions 
 available in Python, such as int. Your function 
 should calculate the result by using the characters in the string.

For now, do not worry about leading + or - signs, nor
should you worry about invalid characters;
 assume all characters are numeric.'''

'''a:
1. take in a string consisting of digits
2. dict_constant of str digits as keys and num digit as value
3. empty num_list to hold each digit
3. loop through string and find matching num from dict
    - num = dict_constant.get(char)
    - num_list.append(num)
4. convert list of nums to a combined int to return
    - .join(?)
'''
DIGITS = {'0': 0, '1': 1, '2' : 2, '3' : 3, '4' : 4, 
              '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9
              }

def string_to_integer(integer, DIGITS):
    num_list = []

# for char in integer add int to list
    for digit in integer:
        num = DIGITS.get(digit)
        num_list.append(num)
    
# reverse int list and add each digit in the list to its proper place order,
#  return final number
    num_list.reverse()
    number = 0
    for index, num in (enumerate(num_list)):
        if index != 0:
            num = num * (10 ** index)
        number += num
    return number

print(string_to_integer("4321", DIGITS) == 4321)  # True
print(string_to_integer("570", DIGITS) == 570)    # True