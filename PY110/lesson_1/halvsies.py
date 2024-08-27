'''Write a function that takes a list as
an argument and returns a list that contains
two elements, both of which are lists. Put 
the first half of the original list elements 
in the first element of the return value and 
put the second half in the second element.

If the original list contains an odd number 
of elements, place the middle element 
in the first half list.
'''

'''a:
1, take in list input
2. calc length
    -store length in var
    if len < 2:
        - if len == 0: return [[][]]
        - else: - if len == 1 
            return[list1[]] ...
3. find half of list
    -length // 2
    -may have do do different for odd..
4. get slices of half store in vars
    -first half
    -second half
5. return list [1sthalf, 2ndhalf]
'''

def halvsies(lst):
    length = len(lst)
    half = ((length + 1) // 2)

    return [lst[:half],lst[half:]]

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])