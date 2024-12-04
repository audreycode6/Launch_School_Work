'''Write a function that computes the difference 
between the square of the sum of the first 'count'
positive integers and the sum of the squares of 
 the first 'count' positive integers.
'''

'''P:
in: integer
out: integer (sum of count) - (sum of count squared)
e:
-count == range(1, integer)
i:
?: doesnt accept negative int
'''

def sum_square_difference(integer):
    count = list(range(1, integer + 1))

    # find sum
    count_sum = sum(count)

    # find sum of squares
    squares = [num ** 2 for num in count]
    sum_squares = sum(squares)

    
    result = count_sum ** 2 - sum_squares
    return result

print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True