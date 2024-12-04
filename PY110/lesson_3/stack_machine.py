'''
A stack is a list of values that grows and shrinks dynamically. 
A stack may be implemented as a list that uses two list methods: list.append and list.pop

 we can talk of pushing things to the stack (adding them to the top of the stack) 
 and popping them from the stack (removing the topmost stack item).

Write a function that implements a miniature stack-and-register-based 
programming language that has the following commands
n: Place an integer value, n, in the register. Do not modify the stack.
PUSH : Push the current register value onto the stack. Leave the value in the register.
ADD : Pop a value from the stack and add it to the register value,
     storing the result in the register.
SUB : Pop a value from the stack and subtract it 
    from the register value, storing the result in the register.
MULT : Pop a value from the stack and multiply it by the 
    register value, storing the result in the register.
DIV : Pop a value from the stack and divide the register value
     by the popped stack value, storing the integer result back in the register.
REMAINDER : Pop a value from the stack and divide the register
     value by the popped stack value, storing the integer remainder of
     the division back in the register.
POP : Remove the topmost item from the stack and place it in the register.
PRINT : Print the register value.
All operations are integer operations (which is only important with DIV and REMAINDER).


Programs will be supplied to your language function via a string argument. 
Your function may assume that all arguments are valid programs -- i.e., 
they will not do anything like trying to pop a non-existent value from
 the stack, and they won't contain any unknown tokens.

Initialize the stack and register to the values [] and 0, respectively.
'''

'''EXAMPLE:
Consider a MULT operation in a stack-and-register language.
It pops the topmost value from the stack, multiplies the 
popped value with the current value in the register, 
then replaces the register content with the result value. 

For example, suppose we start with a stack of [3, 6, 4]
(where 4 is the topmost item in the stack) and a register value of 7, 
the MULT operation mutates the stack to [3, 6] (the 4 is popped), 
and the result of the multiplication, 28, is left in the register. 
If we do another MULT at this point, the stack is mutated to [3],
and the register is left with the value 168.'''


'''
n: Place an integer value, n, in the register. Do not modify the stack.
PUSH : Push the current register value onto the stack. Leave the value in the register.
ADD : Pop a value from the stack and add it to the register value,
     storing the result in the register.
SUB : Pop a value from the stack and subtract it 
    from the register value, storing the result in the register.
MULT : Pop a value from the stack and multiply it by the 
    register value, storing the result in the register.
DIV : Pop a value from the stack and divide the register value
     by the popped stack value, storing the integer result back in the register.
REMAINDER : Pop a value from the stack and divide the register
     value by the popped stack value, storing the integer remainder of
     the division back in the register.
POP : Remove the topmost item from the stack and place it in the register.
PRINT : Print the register value.'''

def minilang(string):
    register = 0
    stack = []
    words = string.split()

    for word in words: # TODO would be more clean to use match/case
        if word == 'PUSH':
            '''Push the current register value onto the stack. 
            Leave the value in the register.'''
            stack.append(register)
        elif word == 'ADD':
            '''Pop a value from the stack and 
            add it to the register value,
            storing the result in the register.'''
            popped_num = stack.pop()
            register += popped_num
        elif word == 'SUB':
            '''Pop a value from the stack and subtract it 
            from the register value, storing the result in the register.'''
            popped_num = stack.pop()
            register -= popped_num
        elif word == 'MULT':
            '''Pop a value from the stack and multiply it by the 
            register value, storing the result in the register.'''
            popped_num = stack.pop()
            register *= popped_num
        elif word == 'DIV':
            ''' Pop a value from the stack and divide the register value
            by the popped stack value, storing the 
            integer result back in the register.'''
            popped_num = stack.pop()
            register //= popped_num
        elif word == 'REMAINDER':
            '''Pop a value from the stack and divide the register
             value by the popped stack value, storing the
            integer remainder of the division back in the register.'''
            popped_num = stack.pop()
            register %= popped_num

        elif word == 'POP':
            '''Remove the topmost item from 
            the stack and place it in the register.'''
            popped_num = stack.pop()
            register = popped_num
        elif word == 'PRINT':
            ''' Print the register value.'''
            print(register)
        else: # is string int
            '''place an integer value, n, in the register. 
            Do not modify the stack.'''
            n = int(word)
            register = n


minilang('PRINT')
# 0

minilang('5 PUSH 3 MULT PRINT')
# 15

minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# 5
# 3
# 8

minilang('5 PUSH POP PRINT')
# 5

minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# 5
# 10
# 4
# 7

minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# 6

minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# 12

minilang('-3 PUSH 5 SUB PRINT')
# 8

minilang('6 PUSH')
# (nothing is printed)