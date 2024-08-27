'''Write a function that takes one argument,
a positive integer, and returns a 
list of the digits in the number.
'''

'''a:
1. take in postive int
2. convert to string
3. convert to list - wasnt needed
4. for element in list convert to int
5. return list of nums
'''
def digit_list(integer):
    return [int(char) for char in str(integer)]

print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True