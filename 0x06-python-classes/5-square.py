#!/usr/bin/python3
class Square:
    """
    This class defines a square with a private instance attribute 'size'.

    A square is a geometric shape with four equal sides and four right angles.
    It is characterized by its side length, which is stored in the 'size' attribute.
    """

    def __init__(self, size=0):
        """
        Initialize a square with the given size. The size should be a non-negative integer.

        Parameters:
        size (int, optional): The length of each side of the square. Default is 0.

        Example:
        square = Square(5)
        """
        self.__size = size

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Example:
        square_size = square.size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square. The size should be a non-negative integer.

        Parameters:
        value (int): The length of each side of the square.

        Example:
        square.size = 6
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
        int: The area of the square.

        Example:
        area = square.area()
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using '#' characters.

        Example:
        square.my_print()
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

