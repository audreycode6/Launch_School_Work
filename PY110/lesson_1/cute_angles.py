'''Write a function that takes a floating point number 
representing an angle between 0 and 360 degrees and 
returns a string representing that angle in degrees, 
minutes, and seconds. You should use a degree symbol (°) 
to represent degrees, a single quote (') to represent minutes, 
and a double quote (") to represent seconds. There are 60 
minutes in a degree, and 60 seconds in a minute.
'''

'''d:
variables for degree, min, sec
- degree: int(angle_input) (0-360, 360 also == 0)
- m = int(angle_input - degree) * 60
- s = (angle_input - degree - min/ 60) * 3600
'''
'''a:
1. take in num input (float)
    - if input - int(input) == 0 than min and sec == 0
    - else continnue with min, sec below
2. convert input to degree
3. convert input to min: 
    if less than 10 add 0 to front
4. convert input to sec
5. return string with degree, min, sec (no space or commas)
'''

DEGREE = "\u00B0"
MINUTES_PER_DEGREE = 60
SECS_PER_DEGREE = 3600

'''helper func format min/sec; if min or sec is less
 than 10 add '0' to front of it to format'''
def format_add_0(min_sec):
    if min_sec < 10: 
        return '0' + str(min_sec)
    return min_sec

'''take in angle number and return the degree,
minutes, and seconds representing that angle'''
def dms(angle_num):
    degree = int(angle_num)
    minutes = int((angle_num - degree) * MINUTES_PER_DEGREE)
    seconds = int((angle_num - degree - (minutes / MINUTES_PER_DEGREE)) * SECS_PER_DEGREE)

    return f"{degree}{DEGREE}{format_add_0(minutes)}'{format_add_0(seconds)}\""

print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0)  == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")
