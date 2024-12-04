'''P:
in: list arg
out; return new list that contains values from input sorted ascending
e:
- using the merge sort algorithm
    - divide into 2 lists: slice1, slice2
    - divide 2 lists into sublist
    - repeat until each sublist contains only 1 value
    -then work way back to add list together, 
        -adding smallest elem to front of sublist until 1 sorted list
        - could use merge func from previos
- dont mutate orig lst
i: -len of lst doesnt have to be even will have odd elem lenth
    - if even len: slice1 = lst[:len(lst)/2]
    - if odd len: 
?: 
algo:
- determine length of list
- get 2 slices of list: 1st hald and 2nd half
- for each slice: continue to slice until just 1 elem in each sublist
'''

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

def merge_sort(lst):
    if len(lst) == 1:
        return lst
    
    sublist_1 = lst[:len(lst) // 2]
    sublist_2 = lst[len(lst) // 2:]

    sublist_1 = merge_sort(sublist_1)
    sublist_2 = merge_sort(sublist_2)

    return merge(sublist_1, sublist_2)


# All of these examples should print True
print(merge_sort([9, 5, 7, 1]) == [1, 5, 7, 9])
print(merge_sort([5, 3]) == [3, 5])
print(merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7])
print(merge_sort([9, 2, 7, 6, 8, 5, 0, 1]) == [0, 1, 2, 5, 6, 7, 8, 9])

original = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
            'Kim', 'Bonnie']
expected = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel',
            'Sue', 'Tyler']
print(merge_sort(original) == expected)

original = [7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54,
            43, 5, 25, 35, 18, 46]
expected = [1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25,
            35, 37, 43, 46, 51, 54]
print(merge_sort(original) == expected)