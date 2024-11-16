import math

radius1 = 30 
radius2 = 40 
 
def calculate_volume_of_sphere(radius): 
return (4 / 3) * math.pi * radius**3 

volume1 = calculate_volume_of_sphere(radius1) 
volume2 = calculate_volume_of_sphere(radius2) 

print("The volume of a sphere with radius", radius1, "is:", round(volume1, 2))
print("The volume of a sphere with radius", radius2, "is:", round(volume2, 2))
