'''Further Exploration
Suppose we alter the problem to look for a number that
 satisfies a condition (e.g., a number greater than 25)
instead of a specific number? Would the current solution 
still work? Why or why not?'''
'''no, would not work with current progrm but you 
could keep get_num_input func and change 
last_num_among to suit the condtion'''

'''helper function: get 6 number inputs with formatted
input messages, return list of inputs'''
def get_num_input():
    numbers = []
    for num in range(1,7):
        if num == 1:
            ending = 'st'
        elif num == 2:
            ending = 'nd'
        elif num == 6:
            num = 'last'
            ending = ''
        else:
            ending = 'th'

        num_input = input(f"Enter the {num}{ending} number: ")
        numbers.append(num_input)

    return numbers

'''main entry point: return message if number inputs meet condition'''
def last_num_among():
    numbers = get_num_input()
    numbers_str = ','.join(numbers)
    condition = '== 0' # # alter condition (> 25) to fit need 

    for num in numbers:
        if int(num) == 0: # alter condition (> 25) to fit need 
            return f"\n Number(s) in {numbers_str} are {condition}." 
    return f"\n{numbers_str} are not {condition}." 

print(last_num_among())


