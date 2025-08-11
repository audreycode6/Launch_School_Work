'''refactor the following program to use separate modules for each of 
the add_point and calculate_reflected_slope functions. 
You should also have a main program file that runs that 
last 4 lines of code shown below.
'''


coordinates = []

def reflect_point(coordinates):
    x, y = coordinates
    return (x, -y)

def add_point(x, y):
    coordinates.append((x, y))

def get_coordinates():
    return coordinates[:]

def calculate_reflected_slope():
    (x2, y2), (x1, y1) = [reflect_point(point) for point in get_coordinates()]
    return (y2 - y1) / (x2 - x1)

add_point(4, 3)
add_point(1, -9)
slope = calculate_reflected_slope()
print(slope)  # Outputs: -4.0