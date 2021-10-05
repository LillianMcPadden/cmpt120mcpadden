# mathfunctions.py
# This function calculates the volume of a sphere given
# the radius

import math

def sphereVolume(radius):
    volume = 4/3 * math.pi * radius ** 3
    return volume

def sphereArea(radius):
    surface_area = 4 * math.pi * radius ** 2
    return surface_area

def main():
    radius = eval(input("Enter the radius of the sphere: "))
    print("The area of the sphere is: ",sphereArea(radius))
    print("The volume of the sphere is:",sphereVolume(radius))

main()
