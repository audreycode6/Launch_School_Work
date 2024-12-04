'''P:
in: 2 sorted lists (all int or string values)
out: new list that contains all the elements from both input lists 
    in ascending order (least to greatest)
e:
- inputs are either all string elems or all int elems
- do not mutate original
- must build result list one element at a time in order
- lists can be empty: if empty list arg only sort non emepty list
i:
?: can i combine the lists first and then sort (?) no
-'You may not provide any solution that requires you to sort the result list. 
You must build the result list one element at a time in the proper order'
    - can i use sort methods(?)


algo:

'''
# def sort_lst(lst1):
#     lst1_copy = lst1.copy()
#     new_lst = []
#     while lst1_copy: # sort list
#         idx = lst1_copy.index(min(lst1_copy))
#         smallest = lst1_copy.pop(idx)
#         new_lst.append(smallest)
#     return new_lst

# def merge(lst1, lst2):
#     if not lst1: # empty 1st arg
#         return sort_lst(lst2)
#     if not lst2: # empty 2nd arg
#         return sort_lst(lst1)
    
#     new_lst = sort_lst(lst1) # sorted 1st arg
#     for elem_2 in lst2: # 
#         for idx, elem_new in enumerate(new_lst):
#             if elem_new > elem_2:
#                 new_lst.insert(idx, elem_2)
#                 break

#     if lst2[-1] not in new_lst:
#         new_lst.append(lst2[-1])

#     return new_lst


def merge(lst1, lst2):
    copy1 = lst1.copy()
    copy2 = lst2.copy()
    new_lst = []

    while copy1 and copy2:
        if copy1[0] <= copy2[0]:
            new_lst.append(copy1.pop(0))
        else:
            new_lst.append(copy2.pop(0))
        
    return new_lst + copy1 + copy2

# All of these examples should print True
print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                  'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)