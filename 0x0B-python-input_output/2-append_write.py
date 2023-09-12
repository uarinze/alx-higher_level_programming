#!/usr/bin/python3
'''function that appends a string at the end of a text file
(UTF8) and returns the number of characters added
'''


def append_write(filename="", text=""):
    '''function that appends a string at the end of a text file
    (UTF8) and returns the number of characters added

    Args:
        filename: name of file
        text: the text to apend

    Return:
        The number of chracters added
    '''
    with open(filename, 'a', encoding='utf-8') as f:
        syz = f.write(text)
    return syz
