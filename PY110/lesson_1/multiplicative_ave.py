'''Write a function that takes a list of positive integers 
as input, multiplies all of the integers together,
divides the result by the number of entries in the list,
and returns the result as a string with the value 
rounded to three decimal places.
'''

'''a:
1. take in list of int
2. find product of elements in list
3. find average: product/ len(list) 
4. average value rounded to 3 decimal places
5. convert to str and return
'''
def multiplicative_average(list):
    product = 1
    for element in list:
        product *= element
    average = product / len(list)

    return f'{average:.3f}'

# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")