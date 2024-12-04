'''P:
in: take in a random MxN matric
out: rotate matrix clockwise by 90 degrees; return results as new matrix
e:
reg 3 x 3matrxi: [
    [0a, 1a, 2a],
    [0b, 1b, 2b],
    [0c, 1c, 2c]
    ]
    VS:
    [
    [0a, 1a, 2a],
    [0b, 1b, 2b]
    ]

90 rotation: [
    [0c, 0b, 0a],
    [1c, 1b, 1a],
    [2c, 2b, 2a]
    ]
    VS:
    [   
        [0b, 0a],
        [1b, 1a],
        [2b, 2a]
    ]

i:
?:
'''


def rotate90(matrix):
    elem_length = len(matrix[0])
    new_lst = []
    
    for idx in range(elem_length):
        inner_lst = []
        for elem in reversed(matrix):
            inner_lst.append(elem[idx])
        new_lst.append(inner_lst)
    return new_lst

matrix1 = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

matrix2 = [
    [3, 7, 4, 2],
    [5, 1, 0, 8],
]

new_matrix1 = rotate90(matrix1)
new_matrix2 = rotate90(matrix2)
new_matrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))))

# These examples should all print True
print(new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]])
print(new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]])
print(new_matrix3 == matrix2)