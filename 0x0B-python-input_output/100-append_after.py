#!/usr/bin/python3
'''function that inserts a line of text to a file,
after each line containing a specific string
'''


def append_after(filename="", search_string="", new_string=""):
    '''function that inserts a line of text to a file,
    after each line containing a specific string

    Args:
        filename: name of file
        search_string: string to search
        new_string: string to add
    '''
    text = ""
    with open(filename, 'r', encoding="UTF-8") as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, 'w', encoding="UTF-8") as f:
        f.write(text)
