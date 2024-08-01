'''Write a program that solicits six (6) numbers from the
user and prints a message that describes whether the sixth
number appears among the first five.'''

'''Further Exploration
Suppose we alter the problem to look for a number that
 satisfies a condition (e.g., a number greater than 25)
instead of a specific number? Would the current solution 
still work? Why or why not?'''

'''helper function: get 6 number inputs with formatted
input messages, return list of inputs'''
def get_num_input():
    ENDINGS = ['1st', '2nd', '3rd', '4th', '5th', 'last']
    numbers = []

    for ending in ENDINGS:
        num_input = input(f"Enter the {ending} number: ")
        numbers.append(num_input)

    return numbers

'''main entry point: return message if last num input
 found within first 5 num inputs '''
def last_num_among():
    numbers = get_num_input()

    last_num = numbers.pop()
    if last_num in numbers: 
        result = 'is'
    else:
        result = "isn't"
    
    numbers_str = ','.join(numbers)

    return f"\n{last_num} {result} in {numbers_str}."

print(last_num_among())




