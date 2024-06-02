#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    size = 0
    '''
    for i in my_list:
        size += 1

    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                size += 1
        except (ValueError, IndexError):
            break
    print()
    return (size)
    '''

    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                size += 1
        print()
    except (ValueError, IndexError):
        print()
    return (size)
