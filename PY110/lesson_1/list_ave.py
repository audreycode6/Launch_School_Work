'''Write a function that takes one argument, 
a list of integers, and returns the average of 
all the integers in the list, rounded down to 
the integer component of the average. The list 
will never be empty, and the numbers will 
always be positive integers.'''

'''a:
1. take in list of ints
2. find sum of all ints in list
3. find average of list: product // len(list)
4. return int average
'''

def average(my_list):
    return sum(my_list) // len(my_list)

print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52])== 40)     # True
print(average([7])== 7)                          # True