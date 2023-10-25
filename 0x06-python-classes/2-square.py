#!/usr/bin/python3
"""
This module containes a Class that
defines a square
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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
