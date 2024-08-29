'''Write a function that takes one argument,
 a positive integer, and returns the sum of its digits.
'''
'''P:
in: postive int
out: int: sum of the digits of positive int
e:
i:
?:
'''

def sum_digits(num):
    return sum([int(digit) for digit in str(num)])

print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True