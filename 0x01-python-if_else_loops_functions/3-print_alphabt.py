#!/usr/bin/python3
for lr in range(97, 123):
    if chr(lr) == 'q' or chr(lr) == 'e':
        continue
    else:
        print("{}".format(chr(lr)), end="")
