#!/usr/bin/python3
"""Defines a class that does the work of magicclass"""

import math


class MagicClass:
    """does the work of magicclass"""

    def __init__(self, radius=0):
        """Initialize a new instance
        Args:
            radius (int or float): A numner"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculates the area"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """gets the circumference"""
        return (2 * math.pi * self.__radius)
