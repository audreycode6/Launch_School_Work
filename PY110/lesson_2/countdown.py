'''Our countdown to launch isn't behaving as expected. 
Why? Change the code so that our program successfully 
counts down from 10 to 1 before launching.
'''

'''P:
in: int: 10
out: print num from int input (10) to 1
'''

''' original to debug: only prints 10
def decrease(counter):
    return counter - 1

counter = 10

for _ in range(10):
    print(counter)
    decrease(counter)

print('LAUNCH!')
'''

''' LS way: assign func invocation to counter variable'''
def decrease(counter):
    return counter - 1

counter = 10

for _ in range(10):
    print(counter)
    counter = decrease(counter)

print('LAUNCH!')

'''My way: fix func by moving range loop inside for loop'''
def decrease(counter):
    for _ in range(counter, 0, -1):
        print(_)

counter = 10
decrease(counter)
print('LAUNCH!')

