#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Get the list of command-line arguments (excluding the script name)
    args = sys.argv[1:]

    # Get the number of arguments
    num_args = len(args)

    # Determine the appropriate string for the number of arguments
    arg_string = "arguments" if num_args != 1 else "argument"

    # Print the number of arguments in the desired format
    if num_args == 0:
        print(f"0 {arg_string}.")
    else:
        print(f"{num_args} {arg_string}:")

        # Print each argument along with its position
        for i, arg in enumerate(args, start=1):
            print(f"{i}: {arg}")
