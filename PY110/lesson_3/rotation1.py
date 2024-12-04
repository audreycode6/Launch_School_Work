''' Write a function that rotates a list by moving the 
first element to the end of the list. Do not modify the original 
list; return a new list instead.

+ If the input is an empty list, return an empty list.
+ If the input is not a list, return None.
Review the test cases below, then implement the solution 
accordingly.'''

'''P:
in: list, or other data 
out: new list: moving 1st elem to end of list/ or None if not list
e:
-if empty list return empty list
- if not list type return None
- can be nested list
i:
?:
'''

def rotate_list(lst):
    new_lst = []
    if not isinstance(lst, list): # handle non list input
        return None
    if lst:
        first_elem = lst[0]
        sliced_lst = lst[1:]
        sliced_lst.append(first_elem)
        new_lst = sliced_lst

    return new_lst

# All of these examples should print True

print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])

# return `None` if the argument is not a list
print(rotate_list(None) == None)
print(rotate_list(1) == None)

# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])