'''problem: Triangles
Write a program to determine whether a triangle is equilateral, isosceles, or scalene.
- An equilateral triangle has all three sides the same length.
- An isosceles triangle has exactly two sides of the same length.
- A scalene triangle has all sides of different lengths.

Note: For a shape to be a triangle at all, 
all sides must be of length > 0,
and the sum of the lengths of any two sides must 
be greater than the length of the third side.'''

'''PEDAC:
P: 
    in: Triangle instance (Triangle(angle1, angle2, angle3))
    out: triangle.kind -> string ("isosceles" , "equilateral", "scalene")
    e:
    - take in instance of triangle (needs 3 sides)
    - identify if equilateral : all sides are ==

    - identify if sum of any 2 sides must be > than 3rd side --> raise ValueError
        - identify if isoscelees: 2 sides same length
        - identify if scalene: all sides !=
    i:
    - identify if any side is less than 1 --> raise ValueError
    - make a triangle class
        - triangle instance has 'kind' attribute (method?) which is set to its triangle type

E: tri_test.py
D:
- make triangle class
    - takes in 3 angles greater than 0
    - kind method:
        returns string identifier of what type or raises error if doesnt fit into triangle category

'''

class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.sides = [side1, side2, side3]

        # raise ValueError if illegal side lengths 
        self.validate_triangle()
    
    @property
    def kind(self):
        if self.is_equilateral():
            return "equilateral"
        if self.is_isosceles():
            return "isosceles"
        if self.is_scalene():
            return "scalene"

    def is_equilateral(self):
        return len(set(self.sides)) == 1
    
    def is_isosceles(self):
        return len(set(self.sides)) == 2

    def is_scalene(self):
        return len(set(self.sides)) == 3

    def validate_triangle(self):
        # raise ValueError if any side is <=0
        for side in self.sides:
            if side <= 0:
                raise ValueError("Side must be greater than 0!")
            
        # raise ValueError if sum of 2 angles is < than 3rd side
        if (
            (sum([self.side1, self.side2]) <= self.side3) or 
            (sum([self.side1, self.side3]) <= self.side2) or 
            (sum([self.side2, self.side3]) <= self.side1)
            ):
            raise ValueError("Sum of 2 sides must be greater than 3rd side")
        '''LS suggestion for improvement
        if not all([
            self.side1 + self.side2 > self.side3,
            self.side1 + self.side3 > self.side2,
            self.side2 + self.side3 > self.side1
        ]):
            raise ValueError("Sum of 2 sides must be greater than 3rd side")
        '''
