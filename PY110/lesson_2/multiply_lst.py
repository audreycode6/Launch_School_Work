'''You want to multiply all elements of a list by 2. 
However, the function is not returning the expected
 result. Explain the bug, and provide a solution.
'''

'''debug original:

def multiply_list(lst):
    for item in lst:
        item *= 2 # isnt mutating lst so when we return lst it returns the unchanged original

    return lst

print(multiply_list([1, 2, 3])) # == [2, 4, 6]) # buggy: [1, 2, 3]
'''

'''solution'''

def multiply_list(lst):
    '''for loop way - non mutating'''
    # new_lst = [] # new lst and append item
    # for item in lst:
    #     item *= 2
    #     new_lst.append(item) 
    
    '''OR list comp - non mutating'''
    # new_lst = [item * 2 for item in lst] # new lst and append item

    # return new_lst
    
    ''' OR enumerate() and mutate original list'''
    for idx, num in enumerate(lst):
        lst[idx] = num * 2
    return lst

print(multiply_list([1, 2, 3]) == [2, 4, 6]) # True