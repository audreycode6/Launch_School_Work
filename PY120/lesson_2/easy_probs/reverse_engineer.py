'''Write a class such that the following code 
prints the results indicated by the comments:
'''
'''TODO:
-create Transfrom class
- initializer takes in string
- TBD Tranform objects should be able to output string
     + chain with methods to alter return
'''

class Transform:
    def __init__(self, string):
        self.string = string
    
    def uppercase(self):
        return self.string.upper()
    
    @classmethod
    def lowercase(cls, str_):
        return str_.lower()

my_data = Transform('abc')
# print(my_data)
print(my_data.uppercase())              # ABC
print(Transform.lowercase('XYZ'))       # xyz
    # use of Transform signals it is a cls method