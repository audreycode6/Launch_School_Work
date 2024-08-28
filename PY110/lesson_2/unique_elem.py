'''From two list arguments, determine the elements that are 
unique to the first list. The return value should be a set.
'''

'''P:
in:2 lists
out: set: unique elements from lists
e:
i:
?:
'''

'''e:
list1 = [3, 6, 9, 12]
list2 = [6, 12, 15, 18]
print(unique_from_first(list1, list2) == {9, 3})
'''

'''D:
difference method or the - operator.
'''

list1 = [3, 6, 9, 12]
list2 = [6, 12, 15, 18]

'''return set with unique elem from l1 and l2'''
def unique_from_first(list1, list2):
    # OR 
    # return set(list1).difference(set(list2))
    return set(list1) - set(list2) 

print(unique_from_first(list1, list2) == {9, 3})
