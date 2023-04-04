"""Writing functions in Utils."""

__author__ = "730480676"


def only_evens(xs: list[int]) -> list[float]:
    """Make a function that tests only even variables."""
    result: list[int] = []
    idx: int = 0
    if len(xs) == 0:
        return []
    while idx < len(xs):
        if xs[idx] % 2 == 0:
            result.append(xs[idx])
        idx += 1
    return result


def concat(list_a: list[int], list_b: list[int]) -> list[int]:
    """Make a function that creates a single lsit from two lists with all integers of the first followed by all integers of the second."""
    idx_a: int = 0
    idx_b: int = 0
    list_c: list[int] = []
    while len(list_a) > idx_a:
        list_c.append(list_a[idx_a])
        idx_a += 1
    while len(list_b) > idx_b:
        list_c.append(list_b[idx_b])
        idx_b += 1 
    return list_c


def sub(uncool_list: list[int], start: int, end: int) -> list[int]:
    """Make a function that takes the range of a list when given two integers."""
    cool_list: list[int] = []
    if len(uncool_list) == 0 or start >= len(uncool_list):  
        return cool_list
    if start < 0:
        start = 0
    if end > len(uncool_list):
        end = len(uncool_list)
    for index in range(start, end):
        cool_list.append(uncool_list[index])
    return cool_list 
      
     
     