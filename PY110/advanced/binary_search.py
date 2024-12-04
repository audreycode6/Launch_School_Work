'''algo
-binary search:
    - check middle elem if object_to_find: 
        -middle elem index = len(lst) // 2

    - if elem == elem_to_find: return idx of elem

    - else (if not) then make new lst: 
        -while middle_elem != elem_to_find or len(lst) > 2: # TODO test
        - reassign lst, discarding the half not needed:
            lst = lst[:middle_idx] if middle_elem > elem_to_find else lst[middle_idx+1:]
        -reassign middle_elem and middle_idx
            middle_elem = lst[len(lst) // 2]
            middle_idx = lst.index(middle_elem)
        - if middle_elem == elem_to_find: return middle_idx # TODO test
        -else: return -1 (not found in lst)
        '''

def binary_search(lst, elem_to_find):
    lst_copy = lst.copy() # save for later to get real elem index
    middle_elem = lst[len(lst) // 2]
    middle_idx = lst.index(middle_elem)
    
    while middle_elem != elem_to_find:
        lst = lst[:middle_idx] if middle_elem > elem_to_find else lst[middle_idx + 1:]
        if len(lst) == 0: # elem_to_find not found within lst
            return -1 
        middle_elem = lst[len(lst) // 2]
        middle_idx = lst.index(middle_elem)

    return lst_copy.index(middle_elem)

# All of these examples should print True
businesses = ['Apple Store', 'Bags Galore', 'Bike Store',
              'Donuts R Us', 'Eat a Lot', 'Good Food',
              'Pasta Place', 'Pizzeria', 'Tiki Lounge',
              'Zooper']
print(binary_search(businesses, 'Pizzeria') == 7)
print(binary_search(businesses, 'Apple Store') == 0)

print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 77) == -1)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 89) == 6)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 5) == 1)

names = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue',
         'Tyler']
print(binary_search(names, 'Peter') == -1)
print(binary_search(names, 'Tyler') == 6)