'''Create a class named Cat that tracks the number of
 times a new Cat object is instantiated. 
 The total number of Cat instances should be
 printed when total is invoked.'''
'''TODO:
-Cat class
- def __init__
- class variable (cat_count) instantiated at 0 and when instance of class created +=1
-total class method: return total cat_count'''
class Cat:
    cat_count = 0

    def __init__(self):
        Cat.cat_count += 1
    
    @classmethod
    def total(cls):
        print(Cat.cat_count)


Cat.total()         # 0

kitty1 = Cat()
Cat.total()         # 1

kitty2 = Cat()
Cat.total()         # 2

print(Cat())        # <__main__.Cat object at 0x104ed7290>
Cat.total()         # 3