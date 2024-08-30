'''We defined a function intending to multiply 
the sum of numbers by a factor. However, the
function raises an error. Why? How would you fix this code?
'''

'''original to debug:

def sum(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(sum(numbers, 2) == 20)

error raised: TypeError: sum() missing 1 required positional argument: 'factor' 
-because defined func with built in func name: sum, the built in func is shadowed,
when using sum within the func [sum(numbers)] it is loking 
for another arg as defined for this sum func [sum(numbers, factor)] '''

'''solution:
rename the function from sum to a better/ unique descriptor like: factor_sum'''
def multiply_sum(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(multiply_sum(numbers, 2) == 20)