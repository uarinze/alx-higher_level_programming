#!/usr/bin/python3
for i in range(97, 122):
    if i == 101 or i == 113:
        pass
    else:
        print("{:c}".format(i), end="")
