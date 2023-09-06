#!/usr/bin/python3
"""prints a text."""


def text_indentation(text):
    """Prints text with 2 new lines after '.', '?', or ':'"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    x = 0
    while x < len(text) and text[x] == ' ':
        x += 1

    while x < len(text):
        print(text[x], end="")
        if text[x] == "\n" or text[x] in ".?:":
            if text[x] in ".?:":
                print("\n")
            x += 1
            while x < len(text) and text[x] == " ":
                x += 1
            continue
        x += 1
