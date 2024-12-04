'''P: 
2 functions:
- func 1 : egyptian()
in: rational number 
out: list of the denominators that are part of an eqyptian fraction representation of the number
e:
- Rational Number is any number that can be represented as the
    result of the division between two integers,
    e.g., 1/3, 3/2, 22/7, etc. 
    The number to the left is called the numerator, and 
    the number to the right is called the denominator.
i:
?:
algo:
- func 2: unegyptian()
in: list of numbers (same format ..?)
out: calculates and returns the resulting rational njmber
e:
- need to use the fraction class provided by the fractions module
- Every rational number can be expressed as an Egyptian Fraction. 
    In fact, every rational number can be expressed as an Egyptian 
    Fraction in an infinite number of different ways. Thus,
    the first group of examples may not show the same values
    as your solution. They do, however, show the expected
    form of the solution.
    The remaining examples merely 
    demonstrate that the output of egyptian can be 
    reversed by unegyptian.
i:
?:
algo:
'''
from fractions import Fraction

def egyptian():
    return

def unegyptian():
    return

# Using the egyptian function
# Your results may differ for these first 3 examples
print(egyptian(Fraction(2, 1)))      # [1, 2, 3, 6]
print(egyptian(Fraction(137, 60)))   # [1, 2, 3, 4, 5]
print(egyptian(Fraction(3, 1)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 230, 57960]

# Using the unegyptian function
# All of these examples should print True
print(unegyptian(egyptian(Fraction(1, 2))) == Fraction(1, 2))
print(unegyptian(egyptian(Fraction(3, 4))) == Fraction(3, 4))
print(unegyptian(egyptian(Fraction(39, 20))) == Fraction(39, 20))
print(unegyptian(egyptian(Fraction(127, 130))) == Fraction(127, 130))
print(unegyptian(egyptian(Fraction(5, 7))) == Fraction(5, 7))
print(unegyptian(egyptian(Fraction(1, 1))) == Fraction(1, 1))
print(unegyptian(egyptian(Fraction(2, 1))) == Fraction(2, 1))
print(unegyptian(egyptian(Fraction(3, 1))) == Fraction(3, 1))