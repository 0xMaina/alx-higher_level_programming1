#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        integer_value = int(value)
        print(integer_value)
        return True
    except (ValueError, TypeError) as e:
        # Print an error message to stderr and return False
        print(f"Exception: {e}", file=sys.stderr)
        return False
