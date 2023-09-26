#!/usr/bin/env python3

# Created by: Lily Carroll
# Created on: Sept/25/2023
# This program calculates the area and perimeter of a rectangle with user input.
import math


def main():
    # Input.
    # Explaining my program to the user.
    print("This program will calculates the area and")
    print("perimeter of a rectangle.")

    # Declaring variables.
    length = int(input("Enter a length of a rectangle (cm): "))
    width = int(input("Enter a width of a rectangle (cm): "))

    # Process.
    # Equations for area and perimeter of rectangle.
    area = length * width
    perimeter = 2 * (length + width)

    # Output
    # Displaying area and perimeter back to the user.
    print("")
    print("Area = {:.2f} cm^2".format(area))
    print("Perimeter = {:.2f} cm".format(perimeter))


if __name__ == "__main__":
    main()
