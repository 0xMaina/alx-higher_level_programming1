#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary:
        # If the key already exists in the dictionary, replace the value
        a_dictionary[key] = value
    else:
        # If the key doesn't exist, add a new key-value pair
        a_dictionary[key] = value
