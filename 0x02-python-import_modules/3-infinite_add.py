#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Get the list of command-line arguments (excluding the script name)
    args = sys.argv[1:]

    # Initialize a variable to store the sum of arguments
    total = 0

    # Loop through the arguments and add them to the total
    for arg in args:
        total += int(arg)

    # Print the result of the addition
    print(total)
