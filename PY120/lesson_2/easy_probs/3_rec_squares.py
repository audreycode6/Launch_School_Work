'''Given the class from the previous problem; 
Write a class called Square that inherits from 
the Rectangle class. The Square class is used like this:'''

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
    
class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

                
'''VS overwriting __init__ and area for square class
 which is more repetitive'''
    # def __init__(self, width):
    #     self._width = width
    
    # @property
    # def area(self):
    #     return self._width ** 2

    
square = Square(5)
print(square.area == 25)      # True