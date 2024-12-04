'''
. A recursive function is one in which 
the function calls itself. For example,
 the following function is a recursive 
 function that computes the sum of all 
 integers between 1 and n:

 A recursive function has three primary qualities:
1. have a base case. This is a condition that tells 
    the function to stop recursing and begin the process 
    of returning to the first call to the function.
2. The function must call itself except when handling the base case.
3.Each recursive call must be "closer" to the base case than the current call. 

Fibonacci sequence follows a simple set of rules:
    F(1) = 1
    F(2) = 1
    F(n) = F(n - 1) + F(n - 2)    (where n > 2)
The base case occurs when the argument is 1 or 2; both of these arguments result in a value of 1.
The Fibonacci function calls itself. In fact, it calls itself twice.
Except when dealing with the base case, each call to the Fibonacci 
function comes closer to the base case. In this case, both F(n - 1)
 and F(n - 2) are closer to the base case than F(n).

'''

'''P:
in: integer
out: 
e:
- write recursive func that calls itself with
-A recursive function is one in which 
the function calls itself
i:
?:
'''
def fibonacci(integer):
    if integer < 3:
        return 1
    return fibonacci(integer - 1) + fibonacci(integer - 2)

print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)     # True