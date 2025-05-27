'''Sum of Multiples PEDAC:
P:
    -in:2 args:
        - natural num, & 
        - set of 1 or + nums -->if no set default set = {3, 5}
    -out: sum of all multiple of the numbers in set 
    that are less than the 1st num
    -e:
        - find multiples of natural num (dont include natural num)
        - get sum of multiples
    -i:
    - return 0 if no multiples / nat num < all nums in set
    -SumOfMultiple class:
        - init takes in any num of args or none, 
        if none default set == {3,5}, else group all args together
        - sum_up_to() class method, takes in nat_num and 
        returns sum of mults
    ?: what is multiple: 
        a product that we get when one number is multiplied by another number. 
        - i.e what numbers multiplied together == natural num
        - for each num in set:
            for each mult from 1 up to natural num:
                result = num * set
                if result == nat_num:
                    append num to list of multiples
                if result > nat_num:
                    break (so it goes to next multipl)
    
E: test_sum_mult.py
D:
'''

class SumOfMultiples():

    def __init__(self, *numbers):
        if numbers:
            self.numbers = numbers
        else:
            self.numbers = {3, 5}

    def to(self, nat_num):
        multiples = set()
        for number in self.numbers:
            for mult in range(1, nat_num):
                # find multiples > natural number
                multiple = number * mult
                if multiple < nat_num:
                    multiples.add(multiple)
                if multiple >= nat_num:
                    break

        return sum(multiples)

    @classmethod
    def sum_up_to(cls, nat_num):
        return cls().to(nat_num)