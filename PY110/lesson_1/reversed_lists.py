'''Write a function that takes a list as an argument
and reverses its elements, in place. That is, mutate
the list passed into the function. The returned 
object should be the same object used as the argument.

You may not use the list.reverse method nor may you 
use a slice ([::-1]).'''

'''a:
1. take in list
2. loop through list backwards and reassign values to opposite index
    - maybe use enumerate to track index and assign elements to opposite index?
3. return mutates/reversed list
'''

def reverse_list(lst):
    '''new list with copy of original lst elements reversed'''
    reversed_copy = []
    for element in lst:
        reversed_copy.insert(0, element)

    '''reassign lst elements to elements in reversed_copy'''
    index = 0
    for element in reversed_copy:
        lst[index] = element
        index += 1

    return lst

list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result == [4, 3, 2, 1])               # True
print(list1 is result)                      # True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
print(list2 is result2)                     # True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3 == ['abc'])                   # True
print(list3 is result3)                     # True

list4 = []
result4 = reverse_list(list4)
print(result4 == [])                        # True
print(list4 is result4)                     # True


# to understand ls way:
def reverse_list2(lst):
    for idx in range(len(lst) // 2): # len(lst) // 2 == middle, range(middle): 0-(middle-1)
    # if odd len then middle doesnt need to be changed
        print(lst[idx], lst[-(idx + 1)]) # 0, -1 -> 1, -2
        print(lst[-(idx + 1)], lst[idx]) # -1, 0 -> -2, 1
        lst[idx], lst[-(idx + 1)] = lst[-(idx + 1)], lst[idx]

    return lst

list1 = [1, 2, 3, 4]
result = reverse_list2(list1)
print(result == [4, 3, 2, 1])               # True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list2(list2)
print(result2 == ['e', 'd', 'c', 'b', 'a']) # True


list3 = ["abc"]
result3 = reverse_list2(list3)
print(result3 == ['abc'])                   # True

list4 = []
result4 = reverse_list2(list4)
print(result4 == [])                        # True