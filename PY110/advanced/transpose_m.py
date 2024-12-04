'''P:
in:
out:
e:
- modifiy the transpose function from previous exercise so 
    it works with an MxN matric with atleast 1 row and 1 colum
i:
- if only 1 element in list (ie list with list element): each elem gets its out list
- if more than 1 element (ie multiple inner lists) new list has 1 inner list per element in inner lists
- each inner list must have same amount of elements
- if only 1 inner list and 1 element within return unchanged
?:

algo: if length  of nested list == 1
    - for each elem in nested_list gets added as own inner list in new_lst
- 
'''

def transpose(nested_lst):
    elem_length = len(nested_lst[0])
    new_lst = []

    for idx in range(elem_length):
        inner_lst = []
        for elem in nested_lst:
            inner_lst.append(elem[idx])
        new_lst.append(inner_lst)

    return new_lst


# All of these examples should print True
print(transpose([[1, 2, 3, 4]]) == [[1], [2], [3], [4]])
print(transpose([[1], [2], [3], [4]]) == [[1, 2, 3, 4]])
print(transpose([[1]]) == [[1]])

matrix_3_by_5 = [
    [1, 2, 3, 4, 5],
    [4, 3, 2, 1, 0],
    [3, 7, 8, 6, 2],
]
expected_result = [
    [1, 4, 3],
    [2, 3, 7],
    [3, 2, 8],
    [4, 1, 6],
    [5, 0, 2],
]

print(transpose(matrix_3_by_5) == expected_result)