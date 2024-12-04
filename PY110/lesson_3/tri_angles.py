''''''

'''P:
in: 3 angles: integers
out: string: representing triables classfication: (only 1 string output)
    -'right', 'acute', 'obtuse', or 'invalid'
e:
-input only ints 
- the arg are in degrees

-Right: One angle is a right angle (exactly 90 degrees).
Acute: All three angles are less than 90 degrees.
Obtuse: One angle is greater than 90 degrees.
-invalid: all 3 angles != 180 degrees OR an angle is <=0:
i:
?: 
'''
RIGHT_ANGLE = 90
def is_180(list_degs):
    '''return True if all 3 angles == 180'''
    return sum(list_degs) == 180 

def is_obtuse(list_degs):
    '''return True if a degree is greater than 90'''
    for deg in list_degs:
        if deg > RIGHT_ANGLE:
            return True
    return False

def triangle(deg1, deg2, deg3):
    list_degs = [deg1, deg2, deg3]

    if ((0 in list_degs) or (not is_180(list_degs))): 
        # any angle == 0 or all angles != 180 -> triangle is invalid
        return 'invalid'
    elif RIGHT_ANGLE in list_degs:
            return 'right'
    elif deg1 < RIGHT_ANGLE and deg2 < RIGHT_ANGLE and deg3 < RIGHT_ANGLE: #acute
        return 'acute'
    elif is_obtuse(list_degs): #'obtuse'
        return 'obtuse'


print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True