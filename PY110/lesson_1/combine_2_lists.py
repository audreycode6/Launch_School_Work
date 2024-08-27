'''Write a function that combines two lists 
passed as arguments and returns a new list 
that contains all elements from both list 
arguments, with each element taken in alternation.

You may assume that both input lists are non-empty, 
and that they have the same number of elements.'''

'''a: using zipped
1. take in 2 lists
2. combine both altenatively: zip(list1, list2)
3. return zipped converted to list (lazy sequence)
'''
'''a: w/out zipped
1. take in 2 lists:
2. insert each element from list2 alternatively to list1's element
    ... for num in range(len(list)):
        new_list.append(list1[idx])
        new_list.append(list1[idx])
3. return new combined list
'''
'''take in 2 list and return new list 
that contains all elements from both list 
arguments, with each element taken in alternation. '''
def interleave(list1, list2):
    new_list = []
    for element in zip(list1,list2):
        new_list.extend(element)
    return new_list

    # OR without zipped
    # new_list = []
    # for index in range(len(list1)):
    #     new_list.extend([list1[index], list2[index]])
    # return new_list

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True
