'''In this code, the `*` operator should compute the *dot product* of the two vectors.
For instance, if you have `Vector(a, b)` and `Vector(c, d)`, 
the dot product is `a * c + b * d`, where `*` and `+` are 
the usual arithmetic operators.

The `abs` function computes the magnitude of a vector. 
If you have a vector `Vector(a, b)`, 
the magnitude is given by `sqrt(a**2 + b**2)`.
You will need the `math` module to access the `sqrt` function. 
Note that `abs` is a built-in function, so you don't want to override 
it entirely; you only want to change its behavior
for `Vector` objects. There's a magic method you can use.

Don't worry about augmented assignment in this exercise.'''

'''P:
in: 2 vectors 
- vector is a tuple with 2 numeric elems: x and y (postive-negative)
ouT: integer
e:
- the * operator should compute the dot product of the 2 vectors
    -ex: Vector(a,b) and Vector(c,d) -dotproduct-> a * c + b * d
- abs() computes magnitude of a vector
    - magnitude of a vector [e.g Vector(a,b)] : sqrt(a**2 + b**2)
    - need math module to access sqrt() func

- dont want to override abs() built in func enitrely; u want to change its behavior for Vactor objects
    - theres a magic method you can use
i:
?:
algo:
'''
import math

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    # __iadd__ method omitted; we don't need it for this exercise
    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)

    def __mul__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        dot_product = (self.x * other.x) + (self.y * other.y)
        return dot_product
    
    def __abs__(self):
        '''square both nums in Vector by self and add together;
        pass to sqrt() and return its return value'''
        magnitude = math.sqrt(((self.x ** 2) + (self.y ** 2)))
        return magnitude

    def __repr__(self):
        x = repr(self.x)
        y = repr(self.y)
        return f'Vector({x}, {y})'

v1 = Vector(5, 12)
v2 = Vector(13, -4)
print(v1 + v2)      # Vector(18, 8)
print(v1 - v2) # Vector(-8, 16) 
print(v1 * v2) # 17
print(abs(v1)) # 13.0 