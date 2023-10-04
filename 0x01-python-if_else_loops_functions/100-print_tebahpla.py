#!/usr/bin/python3
letters = [chr(i) for i in range(97, 123)]
letters.reverse()
res = ""
i = 0
while i < len(letters) - 1:
    res += letters[i]
    res += chr(ord(letters[i + 1]) - 32)
    i += 2
print("{}".format(res), end="")
