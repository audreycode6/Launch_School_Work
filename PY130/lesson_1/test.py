def reduce(callback, iterable, start):
    accum = start
    for elem in iterable:
        accum = callback(elem, accum)

    return accum



# numbers = [1, 2, 4, 8]
numbers = [3, 7, 2, 9, 5]
print(reduce(lambda number, accum: (number**2) + accum, numbers, 0))        

