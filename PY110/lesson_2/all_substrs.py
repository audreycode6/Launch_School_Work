'''Write a function that returns a list of all 
substrings of a string. Order the returned list 
by where in the string the substring begins. 
This means that all substrings that start at index 
position 0 should come first, then all substrings 
that start at index position 1, and so on. Since multiple 
substrings will occur at each position, return the 
substrings at a given index from shortest to longest.

You may (and should) use the leading_substrings 
function you wrote in the previous exercise:'''

'''P:
in: string
ouT: list: all substrs of str
    -for char ins substrs: show all the possible substrs made with it
e:
- start with all posssible subs strs and decrease by beginning char until left with last char
-can use leand_substrs() func
i:
?:
'''

'''E:
expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]
'''

'''d:
slice
len()
'''

'''a:
1. take in string
2. make list of all substrs in string, continue with each letter in string
'''

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

def leading_substrings(string):
    return [string[:num] for num in range(1, len(string)+1)]

'''return list of substrings: all possible substrs for each char in original str'''
def substrings(string):
    all_substrs = [leading_substrings(string[num:]) for num in range(len(string))]

    # convert substring lists into 1 list
    final_list = []
    for lst in all_substrs:
        final_list += lst

    return final_list 

print(substrings('abcde') == expected_result)  # True

'''LS WAY nested for loop or nested comprehsnion'''

def substrings2(string):    
    results = []
    for idx in range(len(string)):
        string_at_idx = string[idx:] # string decreases by 1st char each iteration
        print(string_at_idx)
        # for loop on substrings from current substring options
        for substring in leading_substrings(string_at_idx):
            results.append(substring) 
        print(results)

    # OR NESTED comp way
    # results = [substr for num in range(len(string))
    #           for substr in leading_substrings(string[num:])]

    return results

print(substrings2('abcde') == expected_result)  # True