#!/usr/bin/python3
def uppercase(s):
    for char in s:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert the lowercase character to uppercase using ASCII
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            print(uppercase_char, end='')
        else:
            # For non-lowercase characters, print them as they are
            print(char, end='')

    # Print a new line after processing the entire string
    print()
