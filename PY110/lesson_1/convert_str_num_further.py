''' Write a hexadecimal_to_integer function that converts a
string representing a hexadecimal number to its integer
value. Hexadecimal numbers use base 16 instead of 10, 
and the characters A, B, C, D, E and F (and the lowercase
equivalents) correspond to decimal values of 10-15.
'''
 #changed include hexdecimal (a-f)
HEXA_DIGITS = {'0': 0, '1': 1, '2' : 2, '3' : 3, '4' : 4, 
              '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9,
              'A' : 10, 'B': 11, 'C' : 12, 'D':13, 'E' :14,
              'F': 15
              }

def hexadecimal_to_integer(integer, HEXA_DIGITS):
    num_list = []

# convert each char in integer to matching digit frin HEXA_DIGITS
    for digit in integer: 
        # changed: .upper()
        num = HEXA_DIGITS.get(digit.upper())
        num_list.append(num)
    
# reverse list and raise each digit to power of its index 
# and add together to return final number
    num_list.reverse()
    number = 0
    for index, num in (enumerate(num_list)):
        if index != 0:
            #changed: power of 16
            num = num * (16 ** index)
        number += num
    return number

print(hexadecimal_to_integer('4D9f', HEXA_DIGITS) == 19871)  # True
print(hexadecimal_to_integer('4B6', HEXA_DIGITS) == 1206) # True