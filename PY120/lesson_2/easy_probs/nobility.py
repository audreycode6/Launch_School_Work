''' Apparently some of our users are nobility, 
and the regular way of walking simply isn't
good enough. Nobility struts.

We need a new class Noble that shows the
title and name when walk is called. 
We also require access to name and title;
they are needed for other purposes that we aren't showing here.'''


''' steps for solution:
-create Noble class
- inherits WalkMixin
-properties getters for name and title
- gait method since using walk
- use super() and override walk method to have title in front
'''
# class WalkMixin:
#     def walk(self):
#         return f"{self.name} {self.gait()} forward"

# # NEW 
# class Noble(WalkMixin):
#     def __init__(self, name, title):
#         self._name = name
#         self._title = title
    
#     @property
#     def name(self):
#         return self._name
    
#     @property
#     def title(self):
#         return self._title
    
#     def gait(self):
#         return 'struts'
    
#     def walk(self):
#         return f"{self.title} {super().walk()}"

# class Person(WalkMixin):
#     def __init__(self, name):
#         self.name = name

#     def gait(self):
#         return "strolls"

# class Cat(WalkMixin):
#     def __init__(self, name):
#         self.name = name

#     def gait(self):
#         return "saunters"

# class Cheetah(WalkMixin):
#     def __init__(self, name):
#         self.name = name

#     def gait(self):
#         return "runs"


'''VS: solution from LS
-Noble class created and inherits WalkMixin
-all classes get __str__ method which is passed 
    to walk methodn in walkMixin now instead of name
'''
class WalkMixin:
    def walk(self):
        return f"{self.__str__()} {self.gait()} forward"

# NEW 
class Noble(WalkMixin):
    def __init__(self, name, title):
        self.name = name
        self.title = title
    
    def __str__(self):
        return f"{self.title} {self.name}"
    
    def gait(self):
        return 'struts'

byron = Noble("Byron", "Lord")
print(byron.walk())  # "Lord Byron struts forward"
print(byron.name)    # "Byron"
print(byron.title)   # "Lord"
