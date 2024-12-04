'''A triangle is classified as follows:

Equilateral: All three sides have the same length.
Isosceles: Two sides have the same length, while the third is different.
Scalene: All three sides have different lengths.
To be a valid triangle, the sum of the lengths of 
the two shortest sides must be greater than the 
length of the longest side, and every side must have a length 
greater than 0. If either of these conditions is not satisfied, the triangle is invalid.

Write a function that takes the lengths of the 
three sides of a triangle as arguments and returns one 
of the following four strings representing the triangle's
classification: 'equilateral', 'isosceles', 'scalene', or 'invalid'.
'''

'''P:
in: 3 nums (float or int): == length of the 3 sides
out: 1 string representing the triangles classification: 
    -'equilateral', 'isosceles', 'scalene', or 'invalid'
e:
-Equilateral: All three sides have the same length.
Isosceles: Two sides have the same length, while the third is different.
Scalene: All three sides have different lengths.
To be a valid triangle, the sum of the lengths of 
the two shortest sides must be greater than the 
length of the longest side, and every side must have a length 
greater than 0. If either of these conditions is not satisfied, the triangle is invalid.

i:
?:
'''

def is_invalid(side_lst):
    '''check if max side is > then sum of 2 other sides (i.einvalid)'''
    max_side = max(side_lst) 
    max_idx = side_lst.index(max_side)
    smaller_sides = [side for idx, side in enumerate(side_lst) if idx!=max_idx] 
    return sum(smaller_sides) < max_side

def triangle(side1, side2, side3):
    side_lst = [side1, side2, side3]

    if 0 in side_lst:
        return 'invalid'
    
    elif side1 == side2 == side3:
        return 'equilateral'
    
    elif ((side1 == side2) or (side1 == side3) or (side2 == side3 )):
    # 2 sides same length and 1 different (isosceles)

        # check if max side is > then sum of 2 other sides (i.einvalid)
        if is_invalid(side_lst):
            return 'invalid'
        
        return 'isosceles'
    
    elif ((side1 != side2 and side1 != side3) and
          (side2 != side3)): # all 3 sides are not equal (scalene)
        return 'scalene'

        

print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True