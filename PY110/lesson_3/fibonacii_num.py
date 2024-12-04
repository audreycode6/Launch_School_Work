'''the Fibonacci series is a sequence of numbers in which each
number is the sum of the previous two numbers. The first two
Fibonacci numbers are 1 and 1. The third number is 1 + 1 = 2, 
the fourth is 1 + 2 = 3, the fifth is 2 + 3 = 5, 
the sixth is 3 + 5 = 8, and so on. In mathematical terms,
this can be represented as:
    F(1) = 1
    F(2) = 1
    F(n) = F(n - 1) + F(n - 2)    (where n > 2)

Write a function called fibonacci that computes 
the nth Fibonacci number, where nth is an argument passed to the function:
'''

'''P:
in: int (poditive)
out: the value of ints fibonaci number
e:
-  Fibonacci series is a sequence of numbers in which each
    number is the sum of the previous two numbers
- fib[0] = 1
- fib[1] = 1
-fib[n] = f[-2] + f[-1]
i:
?: no nums less than 1(?)
'''

def fibonacci(integer):
    series = [1, 1]
    if integer < 3:
        return 1
    for num in range(2, integer): 
        # range start is 2 because we already begin with 2 elements in series
        next_num = series[-1] + series[-2]
        series.append(next_num)
    print(series[-1])
    return series[-1] # the final num in series is the fibonacci number for integer

print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True