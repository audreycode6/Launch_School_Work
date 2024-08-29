'''Given two lists of integers of the same length, 
return a new list where each element is the product
of the corresponding elements from the two lists.'''

'''P:
in: 2 args: lists of ints -- same length
out: new list, each elem is product of elements at same index from the 2 lists
e:
- multiply int at same index of both list
- lists are same length
i:
?:
'''

'''d:
zip() to join elements of same index
- enumerate to get index
'''

'''a:
1. take in 2 lsts
2. multiply elements of same index from lists together and add to newlist
    zip() or enumerate()
3. return newlst
'''

'''lst comp + zip() way --more pythonic'''
def multiply_items(lst1, lst2):
    return [num1 * num2
               for num1, num2 in zip(lst1, lst2)]

''' OR lst comp + range(len(lst)) for idx'''
# def multiply_items(lst1, lst2):
#     return [lst1[idx] * lst2[idx] for idx in range(len(lst1))]

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True