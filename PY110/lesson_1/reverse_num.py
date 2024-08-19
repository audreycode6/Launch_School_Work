'''Write a function that takes a positive 
integer as an argument and returns that 
number with its digits reversed.'''

'''P:
in: int: positive int
Out: int: number with digits reversed
e:
-positive nums only
- reverse num input

i:
-single digit: return unchanged
?'s:
'''

'''e:
print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True
'''

'''d:
-coerce to string
-reverse str and return as int
'''

'''a:
1. take in int
2. coerce to str and reverse
3. coerce to int and return
'''
def reverse_number(integer):
    return int(str(integer)[::-1])



print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True