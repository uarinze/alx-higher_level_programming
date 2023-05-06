#!/usr/bin/python3
'''Function reads a text file and prints to stdout'''


def read_file(filename=""):
    ''' This function reads a file's content to stdout'''
    with open(filename, 'r', encoding="UTF-8") as f:
        print(f.read())
