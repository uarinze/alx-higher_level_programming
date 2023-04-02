#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    '''
    This function divides element of list 1 by element of list 2
    Args:
        my_list_1: first list
        my_list_2: second list
        list_length: lenght of new list
    Returns:
        a new list of length list_length
    '''
    new_list = []
    for i in range(list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError):
            print("division by 0")
            res = 0
        except(TypeError):
            print("wrong type")
            res = 0
        except (IndexError):
            print("out of range")
            res = 0
        finally:
            new_list.append(res)
    return (new_list)
