'''Write a function that takes an integer argument
and returns a list containing all integers between
1 and the argument (inclusive), in ascending order.

You may assume that the argument will always
be a positive integer.
'''

'''P:
in: int 
out: list containing all ints between 1 and arg (inclusive, in ascending order)
e:
- return list of #'s: 1- int put in
i:
- if 1 is arg than just return 1
?'s:
'''

'''E:
print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True
'''

'''D:
range(1,input + 1)
'''

'''A:
1. take in int
2. empty list and append num in range (1, input+1)
3. return list with nums 1- num
'''
def sequence(integer):
    return [num for num in range(1, (integer + 1))]
print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True