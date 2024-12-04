'''P:
in: nested list that represents a 3 x3 matrix
- matrix = [
            [1a, 2a, 3a],
            [1b, 2b, 3b],
            [1c, 2c, 3c]
            ]
out: return new nested list which is the  the transpose of the matrix
new_lst = [
        [1a, 1b, 1c],
        [2a, 2b, 2c],
        [3a, 3b, 3c]
        ]
e:
-  transpose of a 3x3 matrix is the matrix that results from exchanging the rows and columns of the original matrix.
- do not modify the original matrix
I:
?:

algo: 
-grab element at 0 index for each element and add as a inner list in new_list
-grab element at 1 index for each element and add as a inner list in new_list
- element at 2 index for each element and add as a inner list in new_list
- return newlist
'''

matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]
def transpose(nested_lst):
    new_lst = []
    idx = 0
    for row in nested_lst:
        inner_lst = []
        for elem in nested_lst:
            inner_lst.append(elem[idx])
        idx += 1
        new_lst.append(inner_lst)
    return new_lst
new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True
