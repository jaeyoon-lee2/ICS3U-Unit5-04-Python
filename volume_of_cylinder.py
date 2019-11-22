#!/user/bin/env python3

# Created by: Jaeyoon (Jay) Lee
# Created on: Nov 2019
# This program calculates the volume of cylinder


import math


def calculate_volume(radius, height):
    # this function calculate the volume of cylinder

    # process
    volume = math.pi * (radius**2) * height

    return volume


def main():
    # this function gets radius and height

    # input
    radius = input("Enter the radius of cylinder (metre): ")
    height = input("Enter the height of cylinder (metre): ")

    try:
        radius_as_int = int(radius)
        height_as_int = int(height)
        if radius_as_int > 0 and height_as_int > 0:
            volume = calculate_volume(height=height_as_int,
                                      radius=radius_as_int)
            print("The volume of cylinder is {} m³".format(volume))
        else:
            print("Theses number are minus")
    except Exception:
        print("Theses are not integers")
    finally:
        print("Thanks for playing")


if __name__ == "__main__":
    main()
