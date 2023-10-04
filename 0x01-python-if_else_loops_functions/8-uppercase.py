#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        order = ord(str[i])
        order = order - 32 if order >= 97 and order <= 122 else order
        print("{}".format(chr(order)), end="")
    print("")
