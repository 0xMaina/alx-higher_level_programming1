#!/usr/bin/python3
"""
This module containes a Class that
defines a sqaue
"""


class Square:
    """
    This class defines a square
    """

    def __init__(self, size=0):
        """ Creates a new square
        Args:
            size: the square size
        """
        self.size = size

    @property
    def size(self):
        """deal with the size attribute"""
        return (self.__size)

    @size.setter
    def size(self, val):
        if not isinstance(val, int):
            raise TypeError("size must be an integer")
        elif val < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = val

    def area(self):
        """ Calculates the square area
        Return: square area
        """
        return (self.__size ** 2)

    def __eq__(self, other):
        """ Compute area of two squares"""
        return (self.area() == other.area())

    def __ne__(self, other):
        """ Compute area of two squares"""
        return (self.area() != other.area())

    def __lt__(self, other):
        """ Compute area of two squares"""
        return (self.area() < other.area())

    def __le__(self, other):
        """ Compute area of two squares"""
        return (self.area() <= other.area())

    def __gt__(self, other):
        """ Compute area of two squares"""
        return (self.area() > other.area())

    def __ge__(self, other):
        """ Compute area of two squares"""
        return (self.area() >= other.area())
