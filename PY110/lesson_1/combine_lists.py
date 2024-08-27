'''Write a function that takes two lists as arguments
and returns a set that contains the union of the
values from the two lists. You may assume that
both arguments will always be lists.
'''

'''a:
take in 2 lists
return set(list1+list2)
'''
def union(list1, list2):
    return set(list1 + list2)
# OR LS: set(list1).union(set(list2))

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True
