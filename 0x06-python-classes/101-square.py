#!/usr/bin/python3
"""
This module containes a Class that
defines a sqaue
"""


class Square:
    """
    This class defines a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Creates a new square
        Args:
            size: the square size
            position: a tuple of integers
        """
        self.size = size
        self.position = position

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
        Return: square area"""
        return (self.__size * self.__size)

    @property
    def position(self):
        """deal with the position attribute"""
        return (self.__position)

    @position.setter
    def position(self, tup):
        if (not isinstance(tup, tuple) or
                len(tup) != 2 or
                not all(isinstance(n, int) for n in tup) or
                not all(n >= 0 for n in tup)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = tup

    def my_print(self):
        """Prints squares with size"""
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for s in range(0, self.__position[0])]
            [print("#", end="") for n in range(0, self.__size)]
            print("")

    def __str__(self):
        """Printing an areadable way"""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for s in range(0, self.__position[0])]
            [print("#", end="") for n in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
