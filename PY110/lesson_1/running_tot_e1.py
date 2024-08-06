'''Write a function that takes a list of numbers and
returns a list with the same number of elements, but
with each element's value being the running total 
from the original list.'''

'''a:
     1. take in list of nums
     2. new empty list to append new elements
     3. update each element in list to be running total (element += element infront)
        - loop through input list; for num in list
        - add num to last element in new list 
        (maybe in begining set to 0 and then updated to [-1])
        - append augmented element to new list
    4. return new list updated with running totals
        '''

''' take in a list of nums and return new list with elements
 updated with running totals '''
def running_total(num_list):
    running_total = []
    for num in num_list:
        if len(running_total) < 1:
            updated_element = num
        else:
            updated_element = num + running_total[-1]
        running_total.append(updated_element)

    # instead of for loop -> Ls way:
        # total = 0
        # for num in nums:
        #     total += num
        #     result_list.append(total)
    return running_total

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True