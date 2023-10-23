#!/usr/bin/python3
def safe_print_integer(value):
    try:
        # Attempt to format and print the value as an integer
        print("{:d}".format(int(value)))
        return True
    except (ValueError, TypeError):
        return False

