'''Given a sequence of integers, filter out instances 
where the same value occurs successively, retaining 
only the initial occurrence. Return the refined sequence.
'''

'''P:
in: list of ints
out: return list of ints with consecutive dupes removed from list
e:
i:
?:
'''

'''d:
-cant use set would be unordered
    -or use set and then for elem in original if ...
- make new empty list and check if last elem == to current elem in new lst if so continue else append'''

def unique_sequence(lst):
    '''for loop way'''
    new_lst = []
    for idx, elem in enumerate(lst):
        '''if 1st elem or if last elem in new_list not same as current elem in original lst '''
        if (idx == 0) or (elem != new_lst[-1]):
            new_lst.append(elem)

    '''lst comp way'''
    new_lst = [elem for idx, elem in enumerate(lst)
               if (idx == 0) or (elem != lst[idx-1])]
    return new_lst 

original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True