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
        1: "I", 4 : 'IV', 5 : 'V', 9 : 'IX' 
        , 10 : 'X', 40 : 'XL', 50 : 'L', 
        90: "XC", 100 : 'C', 400 : 'CD', 
        500 : 'D', 900: 'CM', 1000 : 'M'
                    }
    
    def __init__(self, number):
        self.number = number
        self.remainder = 0
        self.roman_num = ""

    def to_roman(self):
        # if number is sole roman numeral
        if self.number in RomanNumeral.INT_TO_ROMAN.keys():
            return RomanNumeral.INT_TO_ROMAN[self.number]
        
        closest = self.find_closest_but_not_over(self.number)
        self.remainder = self.number - closest
        self.roman_num = RomanNumeral.INT_TO_ROMAN[closest]
        return self.build_remaining_nums(closest)
    
    def build_remaining_nums(self, closest):
        while self.remainder > 0:
            next_roman_num = self.find_closest_but_not_over(self.remainder)
            self.roman_num = str(self.roman_num 
                                 + RomanNumeral.INT_TO_ROMAN[next_roman_num])
            self.remainder -= next_roman_num
        return self.roman_num 

    def find_closest_but_not_over(self, current_num):
        for num in RomanNumeral.INT_TO_ROMAN.keys():
            if num == current_num:
                return num
            elif num < current_num:
                low_close = num
            else: # num > current_num
                return low_close
        return 1000  # highest possible num in dict
        

