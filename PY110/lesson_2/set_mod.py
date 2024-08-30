'''We want to remove certain items from a set
while iterating over it, but the code below 
throws an error. Why is that and how can we fix it?

'''
'''original buggy:
data_set = {1, 2, 3, 4, 5}

for item in data_set:
    if item % 2 == 0:
        # print(f'even {item}')
        data_set.remove(item)
    # print(item)
    # print(data_set)
'''

'''error raised: RuntimeError: Set changed size during iteration
the problem: changing '''
        
'''the solution: instead of removing the elements 
maybe just add elements to new set that follow under the opposite category
OR make copy to use to iterate through elem and identify 
when item needs to be removed from original'''

'''list comp way: '''
data_set = {1, 2, 3, 4, 5}
data_set = {item for item in data_set
           if item % 2 != 0}

print(data_set) # {1, 3, 5}

'''OR make a copy of set and then iterate of copy to find items to remove and alter original '''
import copy

data_set = {1, 2, 3, 4, 5}

for item in data_set.copy():
    if item % 2 == 0:
        data_set.remove(item)

print(data_set) # alters original





