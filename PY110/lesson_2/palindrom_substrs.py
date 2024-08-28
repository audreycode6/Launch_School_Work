'''Write a function that returns a list of all palindromic
 substrings of a string. That is, each substring must 
 consist of a sequence of characters that reads the 
 same forward and backward. The substrings in the 
 returned list should be sorted by their order of 
 appearance in the input string. 
 Duplicate substrings should be included multiple times.

You may (and should) use the substrings function 
you wrote in the previous exercise.

For the purpose of this exercise, you should
consider all characters and pay attention to 
case; that is, 'AbcbA' is a palindrome, but 'Abcba' and 
'Abc-bA' are not. In addition, 
assume that single characters are not palindromes'''

'''P:
in: string
out: list of palindomic substrings from original string, seperated by commas
e:
-list all palindromic substrings of string
    - in order of appearance ininpout stirng
- duplicate substrings should be included multiple times
    - '-madam-did-madam-', 'madam', 'madam-did-madam', 'ada', ...

- if len of substr < 2: pass
i:
?
'''
'''d:
- use last 2 funcs 
- add another func that checks each substr if is palindromic
    -palindromic func: if substr reversed == original substr then palindromic
    - if is add to new list / or keep
    - else: do nothing/ or remove
    -return final
'''
'''a:
    1. pass string to helper func: substrings(string)
    2. make palindrome func
        -for substr in substrings(string):
        - if substr[::-1] == substr:
        - add to new list
    3. return list of palindromic substrs
'''

def leading_substrings(string):
    return [string[:num] for num in range(1, len(string)+1)]

'''return list of substrings: all possible substrs for each char in original str'''
def substrings(string):
    all_substrs = [leading_substrings(string[num:]) for num in range(len(string))]

    final_list = []
    for lst in all_substrs:
        final_list += lst

    return final_list 

def palindromes(string):
    palindomic_substrs = [substr 
                          for substr in substrings(string)
                          if substr == substr[::-1] and len(substr) > 1 ] # if string code be its own func (LS way)
    
    return palindomic_substrs

print(palindromes('abcd')== [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True