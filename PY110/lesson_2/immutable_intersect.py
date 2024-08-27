'''Transform two lists into frozen sets and find their common elements.'''


'''P:
in: 2 lists
out: frozenset of common elements of list above
e:
return frozen set
find common elements

i:
?:
'''

''' E:
list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7, 8]
expected_result = frozenset({8})
print(intersection(list1, list2) == expected_result) # True'''

'''d:
intersection method or the & operator. --> find elements shared
'''
'''a:
'''

list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7, 8]
expected_result = frozenset({8})

''' convert lists to set and use: s1 & s2 or s1.intesection(s2) to find common element
-> construct to frozen set'''
def intersection(list1, list2):
    return frozenset(set(list1) & set(list2)) 
# LS WAY:
# frozenset(list1) & frozenset(list2)

print(intersection(list1, list2))#== expected_result) # True

