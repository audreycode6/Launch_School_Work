'''Write a function that takes two list arguments,
each containing a list of numbers, and returns a new 
list that contains the product of each pair of numbers 
from the arguments that have the same index. You may 
assume that the arguments contain the same number 
of elements.
'''

'''a:
1. take in 2 lists
2. empty list to append products to
3. loop through list in range of len(list):
    - access elemetn at current index of both lists and multiplt together
    - append each product to new list
4. return new list
'''

def multiply_list(list1, list2):
    return [list1[index] * list2[index] for index in range(len(list1))]

# OR for loop (zip or enumerate can also be used)
    # new_list = []
    # for index in range(len(list1)):
    #     product = list1[index] * list2[index]
    #     new_list.append(product)
    # return new_list

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True