#!/usr/bin/python3
class Square:
    """
    This class defines a square with private instance attributes 'size' and 'position'.

    A square is a geometric shape with four equal sides and four right angles.
    It is characterized by its side length, which is stored in the 'size' attribute.
    The 'position' attribute specifies the position of the square.

    'size' should be a non-negative integer.
    'position' should be a tuple of 2 positive integers.

    The 'my_print' method prints the square with '#' characters, considering the position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a square with the given size and position.

        Parameters:
        size (int, optional): The length of each side of the square. Default is 0.
        position (tuple, optional): The position of the square. Default is (0, 0).

        Example:
        square = Square(5, (2, 2))
        """
        self.size = size  # Uses the property setter for size
        self.position = position  # Uses the property setter for position

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

    @property
    def position(self):
        """
        Retrieve the position of the square.

        Example:
        square_position = square.position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square. The position should be a tuple of 2 positive integers.

        Parameters:
        value (tuple): The position of the square as (x, y).

        Example:
        square.position = (2, 2)
        """
        if not (isinstance(value, tuple) and len(value) == 2 and
                isinstance(value[0], int) and isinstance(value[1], int) and
                value[0] >= 0 and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

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
        Print the square with '#' characters, considering the position.

        Example:
        square.my_print()
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

