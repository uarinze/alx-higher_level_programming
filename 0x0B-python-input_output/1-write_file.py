#!/usr/bin/python3
'''function that writes a string to a text file (UTF8)
and returns the number of characters written
'''


def write_file(filename="", text=""):
    '''function that writes a string to a text file (UTF8)
    and returns the number of characters written
    Args:
        filename: the name of the file
        text: the text to write to file

    Return: the number of charaters written
    '''
    with open(filename, 'w', encoding="utf-8") as f:
        ret = f.write(text)
    return ret
