'''P:
in: list
out: return sorted list -mutate
e:
-sort list using bubble sort algo
- bubble sort works by making multiple passes (iterations) through a list.
    -On each pass, the two values of each pair of consecutive elements
    are compared. If the first value is greater than the second, the 
    two elements are swapped. This process is repeated until a complete
    pass is made without performing any swaps. At that point,
    the list is completely sorted.

- sort by ascending (smallest to greatest)
- compare each consecutive elem with on another and if first elem is bigger it is swapped to right; else stay
- when all sorted smallest to greatest then all done
- list contains atleast 2 elems
- also have to sort names
i:
?:
'''
def swap(lst):
    for idx, elem in enumerate(lst):
        penult_idx = len(lst) - 2
        if idx >= penult_idx: # if current idx is penult idx
            if elem > lst[-1]: 
                lst[idx], lst[-1] = lst[-1], elem
            else: # penult elem and last elem remain in same order
                break
        else: # idx is less than penult idx
            next_idx = idx + 1
            if elem > lst[next_idx]:
                lst[idx], lst[next_idx] = lst[next_idx], elem
    return lst

def bubble_sort(lst):
    # compare each element in list:
    for elem in lst:
        swap(lst)

    return lst

lst1 = [5, 3]
bubble_sort(lst1)
print(lst1 == [3, 5])                   # True

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)                 # True