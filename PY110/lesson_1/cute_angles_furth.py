'''Further:
Our solution only works with positive numbers in 
the range of 0 to 360 (inclusive). Can you refactor 
it so that it works with any positive or negative number?
Our solution has the following results for
 inputs outside the range 0-360:
 
 Since degrees are normally restricted to the range 0-360, 
 can you modify the code so it returns a value in the 
 appropriate range when the input is less than 0 or 
 greater than 360?
'''
'''e:
print(dms(-1))   # 359°00'00" -> 360 + -1
print(dms(400))  # 40°00'00" -> 400 - 360
print(dms(-40))  # 320°00'00" -> 360 + -40
print(dms(-420)) # 300°00'00" -> (360 * 2) + - 420 
'''
'''
d:
if elif else condition: 
    - 360 <= angle >= 0: degree = original way -> int(angle)
    - angle > 360: degree = angle - 360
    - angle < -360: (360 * 2) + angle
rest stays same for getting min and sec ..?
'''

DEGREE = "\u00B0"
MINUTES_PER_DEGREE = 60
SECS_PER_DEGREE = 3600
MAX_DEGREE = 360 # changed

'''helper func format min/sec; if min or sec is less
 than 10 add '0' to front of it to format'''
def format_add_0(min_sec):
    if min_sec < 10: 
        return '0' + str(min_sec)
    return min_sec

'''take in angle number and return the degree,
minutes, and seconds representing that angle'''
def dms(angle_num):
    if 360 >= angle_num >= 0: # original but changed to if condition
        degree = int(angle_num)
        minutes = int((angle_num - degree) * MINUTES_PER_DEGREE)
        seconds = int((angle_num - degree - 
                       (minutes / MINUTES_PER_DEGREE)) * SECS_PER_DEGREE)
    else: # changed
        if angle_num > MAX_DEGREE:
            degree = int(angle_num - MAX_DEGREE)
        elif angle_num < -MAX_DEGREE:
            degree = (MAX_DEGREE * 2) + angle_num 
        else:
            degree = angle_num + MAX_DEGREE
        minutes = 0
        seconds = 0
    
    return f"{degree}{DEGREE}{format_add_0(minutes)}'{format_add_0(seconds)}\""

print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0)  == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")
print(dms(-1) == "359°00'00\"")
print(dms(400) == "40°00'00\"")
print(dms(-40) ==  "320°00'00\"")
print(dms(-420) == "300°00'00\"")
