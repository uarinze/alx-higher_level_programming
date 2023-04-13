#!/usr/bin/python3


class MyList(list):
    """The class MyList inherits from list class"""

    def print_sorted(self):
        """Prints sorted list in ascending order"""
        print(sorted(self))
