'''Create a Rectangle class whose initializer takes two arguments that 
represent the rectangle's width and height, respectively. 
Use the following code to test your solution:

A rectangle's area is given by its width times its height.
'''
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
    
    @property
    def area(self):
        return self._width * self._height

rect = Rectangle(4, 5)

print(rect.width == 4)        # True
print(rect.height == 5)       # True
print(rect.area == 20)        # True