'''Given two lists, convert them to sets and return a 
new set which is the union of both sets.
'''

'''P:
in: 2 lists
out: new set which is union of both sets
e:
-2 lists and conver to sets and return new set
i:
?:
'''

'''e:
list1 = [3, 5, 7, 9]
list2 = [5, 7, 11, 13]
print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})
# Prints True
'''

list1 = [3, 5, 7, 9]
list2 = [5, 7, 11, 13]

'''uses |: combines the elements of two sets, 
collecting all unique elements from both sets '''
def merge_sets(list1, list2):
    return set(list1) | set(list2)

print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})

# OR 1st try:
joined_lists = list1 + list2 # but doesnt necessarily get converted to sets before ...
print(set(joined_lists))
# OR .union() method (same as |)
print(set(list1).union(set(list2)))
