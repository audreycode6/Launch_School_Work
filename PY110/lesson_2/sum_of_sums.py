'''Write a function that takes a list of numbers
and returns the sum of the sums of each leading 
subsequence in that list. Examine the examples to
see what we mean. You may assume that the list 
always contains at least one number.
'''

'''P:
in: list of num
out: return int: sum of the sums of each leading subsequence in lst
E:
-assume that the list 
    always contains at least one number.
- 1st num: 1st_num, 2nd num: 1stnum + 2nd_num, 3rd : 1 + 2 + 3 index
- for each index add the nums infront, add all together to get sum of all sums
i:
?:
'''

'''D:
for num in enumerate(lst):
    add index to index_lst
    if index = 0: sum += elem
    add sum to list

wrap list with sum and return that int
'''

def sum_of_sums(lst):
    sum_lst = []
    sums = 0
    for num in lst:
        sums += num
        sum_lst.append(sums)
        # OR initialize another int instead of sum_lst and augment to add sums
        # prevents the use of sum()
  
    return sum(sum_lst)

print(sum_of_sums([3, 5, 2]) == 21)               # True
# (3) + (3 + 5) + (3 + 5 + 2) --> 21

print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

print(sum_of_sums([4]) == 4)                      # True