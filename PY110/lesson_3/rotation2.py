'''Write a function that rotates the last count 
digits of a number. To perform the rotation, move 
the first of the digits that you want to rotate to 
the end and shift the remaining digits to the left.
'''
'''P:
in: 2 args: number and right_most_count
out: rotate the last count digits of a number
e:
- rotation: move 1st digits to end and remaining digits to left
i:
?: last count digits (?)
should it work with all numbers besides these test cases?
'''
def rotate_ending(right_idx, string_num):
    nums_to_rotate = string_num[-right_idx:]
    rotated = nums_to_rotate[1:] + nums_to_rotate[0]
    return rotated


def rotate_rightmost_digits(num, right_idx):
    string_num = str(num)

    # grab slice before right_idx
    nums_before = string_num[:-right_idx]
    # print(nums_before)

    # grab the right_idx and trailing digits
    rotated_ending = rotate_ending(right_idx, string_num)
    # print(rotated_ending)

    # put beginning and ending together
    final = nums_before + rotated_ending
    return  int(final)




print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True
print(rotate_rightmost_digits(1200, 2) == 1200)      # True