'''Write a function that takes a string argument 
consisting of a first name, a space, and a last name. 
The function should return a new string consisting of 
the last name, a comma, a space, and the first name.

You may assume that the names don't include middle
names, initials, or suffixes ("Jr.", "Sr.").
'''

'''A:
1. take in name str
2. use split to place names in list
    -list[0] = first
    -list[1] = last
3. concate strin from list
    -lastname + ', '
    -first name
'''

def swap_name(name_str):
    list_strs = name_str.split()

    return list_strs[1] + ', ' + list_strs[0]
print(swap_name('Joe Roberts') == "Roberts, Joe")   # True

'''Further Exploration:
Suppose the named person has one or more middle names?
Refactor the current solution so it can accommodate this. 
The middle names should be listed after the first name:
'''

def fe_swap_name(str_name):
    list_names = str_name.split()
    middle_names = ' '.join(list_names[1:-1])

    return f'{list_names[-1]}, {list_names[0]} {middle_names}'
print(fe_swap_name('Karl Oskar Henriksson Ragvals')
                == "Ragvals, Karl Oskar Henriksson")  # True