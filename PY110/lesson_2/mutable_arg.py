'''We want to create a function that appends
a given value to a list. However, the function 
seems to be behaving unexpectedly:
How would you fix this code?
'''

def append_to_list(value, lst=[]):
    lst.append(value)
    return lst

# print(append_to_list(1)) # == [1]) # True  # buggy: [1]
# print(append_to_list(2)) # == [2]) # False # [1,2]
# print(append_to_list(3)) # == [2]) # False # [1,2, 3]
# print(append_to_list(3, [])) # == [3]) # True # [3]

'''The bug:
lst is created the first time it is called without
a lst arg so after lst is initialized it 
continues to be mutated with the value arg when the default arg is used
'''
'''The solution:
fix default arg to None and provide if
condition to create new lst to append to if lst arg not provided
just initialize lst within func 
so it only initialized within local scope and 
doesn't continue to get used in future functions'''

def append_to_list(value, lst = None):
    if lst == None:
        lst = []
    lst.append(value)

    return lst 

print(append_to_list(1)) # == [1])# True, [1]
print(append_to_list(2)) # == [2]) # True, [2]
print(append_to_list(3)) # == [3]) # True, [3]
print(append_to_list(3, [])) # == [3]) # True # [3]