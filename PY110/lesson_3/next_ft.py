

'''P:
in: integer (doesnt have to be feature num)
out: next featured number greater than the int input; 
    -else error message if no next feature number
e:
- featured number (something unique to this exercise) is an 
    odd number that is a multiple of 7, with all of 
    its digits occurring exactly once each.
- The largest possible featured number is 9876543201.
i:
?:

algo: 
find the next featured num
condtions for ft num: 
    - odd: num % 2 != 0 (TODO)
    - multiple of 7: num % 7 == 0 (TODO)
    - all num digts occur just once: for num in str(num) -> if str(num).count(num) == 1 
'''


LARGEST_FT = 9876543201


def no_dupe_digits(num):
    string_num = str(num)
    for char in string_num:
        if string_num.count(char) != 1:
            return False
    return True


def is_ft_num(integer):
    if ((integer % 2 != 0) and # odd
        (integer % 7 == 0) and # multiple of 7
        (no_dupe_digits(integer)) # no duplicate digits
        ):
        return True
    return False


def next_featured(integer):
    '''start with integer and increase by 1 until:
        is_ft_num(start) == True
        or start > LARGEST_FT
        return start or error message
    '''
    start = integer + 1
    error = ("There is no possible number that "
         "fulfills those requirements.")

    while True:
        if is_ft_num(start):
            break
        
        elif start > LARGEST_FT:
            return error
        start += 1

    return start

print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True