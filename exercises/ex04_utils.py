"""Utility using list functions."""
__author__ = "730480676"


def all(num_list: list[int], some_num: int) -> int:
    """Def all fn."""
    if len(num_list) == 0:
        return False
    idx = 0
    while idx < len(num_list):
        if num_list[idx] == some_num:
            idx += 1
        else:
            return False
    return True 


def max(input: list[int]) -> int:
    """Def max fn."""
    maxid: int = 0
    max_int = input[maxid]
    if len(input) == 0:
        raise ValueError("max () arg is an empty list")
    while len(input) > maxid:
        if input[maxid] > max_int:
            max_int = input[maxid]
        maxid += 1 
    return max_int


def is_equal(list_a: list[int], list_b: list[int]) -> int:
    """Def is_equal fn."""
    if len(list_a) != len(list_b):
        return False
    if len(list_a) == 0 and len(list_b) == 0:
        return True
    idx = 0
    if len(list_a) != len(list_b):
        return False
    while idx < len(list_a) and idx < len(list_b):
        if list_a[idx] == list_b[idx]:
            idx += 1
        else: 
            return False 
    return True 