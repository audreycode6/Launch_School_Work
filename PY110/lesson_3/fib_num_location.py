'''P
in: integer : specifies the # of digits  (postive and >= 2)
outs: returns the index of the 1st fibo number that has thge # of digits specifief by the arg
e:
- may assume that the argument is always an integer greater than or equal to 2.
- import the sys module, then we call sys.set_int_max_str_digits
     with the maximum digits desired for string conversion.
i:
?:

find the first fibo num that is the firt instance of integer_digits

d:
- convert fibo num to str and if len of str == integer then return fibo num
- dict: key = int, value = fibo(int)


num = 1 to start and num grows by 1 each time if condtion is falsy (ie str(fib(num)) != integer

'''

import sys

sys.set_int_max_str_digits(50_000)

memo_int = {} # store integer as key and its fibo number as value
def fibonacci(integer):
    if integer < 3:
        return 1
    elif integer in memo_int.keys(): # if key exists then integer fibo already stored 
        return memo_int[integer] 
    else: # integer fibo not stored yet so add key valye pair to dict
        memo_int[integer] = fibonacci(integer - 1) + fibonacci(integer - 2)
        return memo_int[integer]

def find_fibonacci_index_by_length(length):
    num = 1
    while True:
        if len(str(fibonacci(num))) != length:
            num += 1
        else:
            return num


# All of these examples should print True
# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)

# Next example might take a little while on older systems
print(find_fibonacci_index_by_length(10000) == 47847)