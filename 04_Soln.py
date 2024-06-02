# Function Returning Multiple Values
# Create a function that returns both the area and circumference of a circle given its radius.

import math

def circle_stats(radius):
    area = math.pi * radius ** 2 # area = pi r**2 where pi = 3.14 or math.pi also
    circumference = 2 * math.pi * radius 
    return area, circumference

a, c = circle_stats(5)
 
print("Area of circle is: ", a, "circumference is: ", c)