'''A circular buffer is a collection of objects
stored in a buffer that is treated as though
it is connected end-to-end in a circle. 
When an object is added to this circular buffer, 
it is added to the position that immediately follows
the most recently added object, while removing an 
object always removes the object that has been in the buffer the longest.

This works as long as there are empty spots in the buffer.
If the buffer becomes full, adding a new object 
to the buffer requires getting rid of an existing object;
with a circular buffer, the object that has been in 
the buffer the longest is discarded and 
replaced by the new object.
'''

''' write a CircularBuffer class in Python 
that implements a circular buffer for arbitrary objects. 
The class should be initialized with the buffer size 
and provide the following methods:

put: Add an object to the buffer
get: Remove (and return) the oldest object in the buffer. 
    Return None if the buffer is empty.
You may assume that none of the values stored in the buffer 
    are None (however, None may be used to designate empty spots in the buffer).
'''
'''
- track oldest item in buffer, -update when item removed
- put method: 
    - takes in object and adds in place of oldest if buffer full 
    - else (if buffer not full) add to next available space
    - use a list the size of spots
        to track items added (update and reomve items )
'''

class CircularBuffer:
    def __init__(self, spots):
        self.spots = spots
        self.buffer = [None] * spots 
        self.oldest = 0
        self.next = 0
        self.items = 0

    def put(self, item): # add an object to buffer
        if self.items == self.spots: 
            self.oldest = (self.oldest + 1) % self.spots
        else: 
            self.items += 1 

        self.buffer[self.next] = item 
        self.next = (self.next + 1) % self.spots 
                    

    def get(self): # remove and return oldest object in buffer
        if self.items == 0: 
            return None
        
        oldest_item = self.buffer[self.oldest] 
        self.buffer[self.oldest] = None 
        self.oldest = (self.oldest + 1) % self.spots
        self.items -= 1
        return oldest_item
        

buffer = CircularBuffer(3)

print(buffer.get() is None)          # True 

buffer.put(1) 
buffer.put(2) 
print(buffer.get() == 1)             # True

buffer.put(3)
buffer.put(4)
print(buffer.get() == 2)             # True

buffer.put(5)
buffer.put(6)
buffer.put(7)
print(buffer.get() == 5)             # True
print(buffer.get() == 6)             # True
print(buffer.get() == 7)             # True
print(buffer.get() is None)          # True

buffer2 = CircularBuffer(4)

print(buffer2.get() is None)         # True

buffer2.put(1)
buffer2.put(2)
print(buffer2.get() == 1)            # True

buffer2.put(3)
buffer2.put(4)
print(buffer2.get() == 2)            # True

buffer2.put(5)
buffer2.put(6)
buffer2.put(7)
print(buffer2.get() == 4)            # True
print(buffer2.get() == 5)            # True
print(buffer2.get() == 6)            # True
print(buffer2.get() == 7)            # True
print(buffer2.get() is None)         # True
