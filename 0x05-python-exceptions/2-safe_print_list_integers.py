#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list that are integers.
    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.
    Returns:
        The number of elements printed.
    """
    size = 0
    for i in range(x):
        try:
            if isinstance(my_list, int):
                print("{:d}".format(my_list[i]), end="" )
                size += 1
        except:
            size += 1
            continue
    print()
    return (size)

