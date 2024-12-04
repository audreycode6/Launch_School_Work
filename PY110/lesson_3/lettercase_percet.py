'''Write a function that takes a string and returns 
a dictionary containing the following three properties:

the percentage of characters in the string that are lowercase letters
the percentage of characters that are uppercase letters
the percentage of characters that are neither
All three percentages should be returned as strings whose numeric
 values lie between "0.00" and "100.00", respectively. 
 Each value should be rounded to two decimal points.

You may assume that the string will always contain at least one character.'''

'''P:
in: string
out: dictionary containig the following properties:
    -the percentage of characters in the string that are lowercase letters
    -the percentage of characters that are uppercase letters
    -the percentage of characters that are neither
e:
- all 3 perecentagies should be returned as strings whose numeric value is beteeen '0.00' and '100.00'
    - only 2 decimal points: {string.2f}
-string always contains at least 1 char (no empty input)
i:
?:
'''


def letter_percentages(string):
    # create dictionary to store keys and values
    percentages = {}
    length = len(string) # how many total chars

    # find how many chars are lower ,upper, neither
    lower_count = 0
    upper_count = 0
    neither = 0
    for char in string:
        if char == char.lower() and char.isalpha():
            lower_count += 1
        elif char == char.upper() and char.isalpha():
            upper_count += 1
        else:
            neither += 1

    # convert lower, upper, niehter to percentages 
    lower_percent = (lower_count / length) * 100
    upper_percent = (upper_count / length) * 100
    neither_percent = (neither / length) * 100

    # convert to stirng and + format decimal place by rounding 2
    str_lower = f'{lower_percent:.2f}'
    str_upper = f'{upper_percent:.2f}'
    str_neither = f'{neither_percent:.2f}'
   
    # add keys (lower, upper, niehter) and their values(percentage) to dictionary (percentages)
    percentages['lowercase'] = str_lower
    percentages['uppercase'] = str_upper
    percentages['neither'] = str_neither
 
    return percentages


expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)