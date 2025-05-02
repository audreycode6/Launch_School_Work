'''problem: roman numerals
Write some code that converts modern decimal numbers 
    into their Roman number equivalents.

The Romans were a clever bunch. 
    They conquered most of Europe and ruled it 
    for hundreds of years. They invented concrete 
    and straight roads and even bikinis. One thing 
    they never discovered though was the number zero. 
    This made writing and dating extensive histories of 
    their exploits slightly more challenging, but the 
    system of numbers they came up with is still in use 
    today. For example the BBC uses Roman numerals to date 
    their programmes.

The Romans wrote numbers using letters - I, V, X, L, C, D, M. 
    Notice that these letters have lots of straight lines and 
    are hence easy to hack into stone tablets.
        1  => I
        10  => X
        7  => VII
 
There is no need to be able to convert numbers 
    larger than about 3000. 

Wikipedia says: Modern Roman numerals ... 
    are written by expressing each digit separately starting
      with the left most digit and skipping any digit with a
        value of zero.

To see this in practice, consider the example of 1990. 
    In Roman numerals, 1990 is MCMXC:
        1000=M
        900=CM
        90=XC

    2008 is written as MMVIII:
        2000=MM
        8=VIII
'''
'''PEDAC:
P:
    in: integer
    out: return string -> 
        the number converted to roman numeral
    e:
    - need RomanNumeral class that take in number
    - has method to_roman() that returns the roman numeral for instance 
        of RomanNumeral
    - figure out formula for converting number to roman numeral 
        - look at each number in the int from left to right


            - 'I' == 1, and up to 3 (I, II, II)
            - 'V' == 5,  
            - placing 'I' (or any smaller num) infront of 'V' (any larger num)
                indicates subtraction (e.g IV == 4)
            - 'X'  == 10 (IX == 9)
            - 'L' == 50
                - XL == 40 (50-10)
            - 'C' == 100
            - 'D' == 500
            - 'M' == 1000
            - only doing up to 3000
    i:
    
E: test_roman.py
D: 
- use dict to store key the num and value roman_num'''

class RomanNumeral:

    INT_TO_ROMAN = {
        "M" : 1000, 
        "CM" : 900,
        "D" : 500,
        "CD" : 400,
        "C" : 100,
        "XC" : 90,
        "L" : 50,
        "XL" : 40,
        "X" : 10,
        "IX" : 9,
        "V" : 5,
        "IV" : 4,
        "I" : 1,
    }    
    def __init__(self, number):
        self._number = number

    @property
    def number(self):
    # discourage reassignment of number value by only defining a getter
        return self._number

    def to_roman(self):
        roman_version = ''
        remaining_value = self.number 

        while remaining_value > 0:
            for roman_numeral, integer in RomanNumeral.INT_TO_ROMAN.items():
                if remaining_value >= integer:
                    # reassign remaining_value: deduct value we will be adding to string
                    remaining_value -= integer 
                    # reassign roman_version: add the next roman_numeral
                    roman_version += roman_numeral
                    # break out of the if condition once above reassignments done
                    #  so that we always search from highest roman numeral int
                    break

        return roman_version

