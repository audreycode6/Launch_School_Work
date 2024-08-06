'''In this exercise, you're going to extend previous func
(num_to_str.py) by adding the ability to represent
negative numbers as well.

Write a function that takes an integer and converts it 
to a string representation.

You may not use any of the standard conversion 
functions available in Python, such as str. You may,
however, use integer_to_string from the previous exercise.'''

'''a:
1. check 1st char (- or # or 0)
    - if -: add '-' to front of final
    - if #: add '+' to front of final
    - if == 0: return '0'
2. turn integer to absolute form
3. helper func on absolute int
4. return int with sign at front
'''

'''main entry point: return '0' or int_str with (-/+) sign'''
def signed_integer_to_string(integer):
    if integer == 0:
        return '0'
        
    sign = '-' if integer < 0 else '+'
    int_str = integer_to_string(abs(integer))

    return sign + int_str

'''Helper func: convert int to string'''
def integer_to_string(integer):
  int_str = ''
  DIGIT_CHARS = ['0','1','2','3','4','5','6','7','8','9']

  while integer > 0:
      integer, remainder = divmod(integer, 10)
      int_str = DIGIT_CHARS[remainder] + int_str

  return int_str

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True

