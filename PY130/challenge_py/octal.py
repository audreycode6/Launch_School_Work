'''Octal: PEDAC
P:
    in: octal string
    out: int -> a decimal output (?)
    e:
    - only valid digits are (0, 1, 2, 3, 4, 5, 6, 7)
    - treat invalid digits as octal 0 (aka 1)
    - implement conversions ourself
    -decimal is a base-10 system, linear combo of powers
        - octal_digit = 0
        - for idx, char in enumerate(string[::-1]): 
        # start from last digit to first
            - if char.isalpha() or int(char) not in VALIDDIGITS:
                char = 1
            - else:
                char = int(char)

            # do conversion:
            new_digit = char*8^idx
            octal_digit += newdigit  
    i:
    - Octal class, takes in string at input
        - to_decimal() class method:
            - 
    ?:
        -what is octal 0 --> 1(?) (8**0)
E: test_octal.py
D:
'''

class Octal():
    VALID_DIGITS = [0, 1, 2, 3, 4, 5, 6, 7]

    def __init__(self, string):
        self.string = string

    def to_decimal(self):
        result = 0

        if not self.string.isnumeric():
            return result

        for idx, char in enumerate(self.string[::-1]):
            if int(char) not in Octal.VALID_DIGITS:
                return result

            char = int(char)
            new_digit = char * (8 ** idx)
            result += new_digit

        return result
