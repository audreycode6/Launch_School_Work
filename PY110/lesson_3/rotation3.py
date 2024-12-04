'''Take the number 735291 and rotate it by one digit to the left, 
getting 352917. Next, keep the first digit fixed in place and 
rotate the remaining digits to get 329175. Keep the first two 
digits fixed in place and rotate again to get 321759. 
Keep the first three digits fixed in place and rotate again
 to get 321597. Finally, keep the first four digits fixed 
 in place and rotate the final two digits to get 321579. 
 The resulting number is called the maximum rotation of the original number.

Write a function that takes an integer as an argument and
 returns the maximum rotation of that integer. You can 
 (and probably should) use the rotate_rightmost_digits
 function from the previous exercise.
'''

'''P:
in: integer
ouT: maximum rotation of that int
e:
- can use the function from last problem
- 1st char moves to index [-1]
-new 3rd char 
I:
?:
 '''

def max_rotation(inty):
    list_nums = list(str(inty))

    new_lst = list_nums.copy()
    for idx, num in enumerate(list_nums):
        char = new_lst.pop(idx)
        new_lst.append(char)
    string_num = ''
    for char in new_lst:
        string_num += char

    return int(string_num)

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True