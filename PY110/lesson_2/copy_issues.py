'''We have a list of lists and want to duplicate it.
After making the copy, we modify the original list,
but the copied list also seems to be affected:

What's wrong here? How can you fix it?
'''

'''the buggy:
import copy

original = [[1], [2], [3]]
copied = copy.copy(original)

original[0][0] = 99

print(copied[0]) # == [1]) # actually: [99]

the problem: using copy on a nested list it only copies the outer layer 
the inner layers are a shadow copy and continue and will continue to 
be effected if changes are made the the inner elements (bc they continue to reference original objs)'''

'''the solution:
use deepcopy to ensure all inner and outer levels are 
copied so that it cannot be affect by changes to the original'''
import copy

original = [[1], [2], [3]]
copied = copy.deepcopy(original)

original[0][0] = 99

print(copied[0] == [1]) # True