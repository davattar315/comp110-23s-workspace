"""A series of dictionary based functions."""
__author__ = "730480676"


def invert(vdict_1: dict[str, str]) -> dict[str, str]:
    """A function which inverts the values of a dict."""
    new_dict: dict[str, str] = {}
    for key in vdict_1:
        new_value = vdict_1[key]
        if new_value in new_dict:
            raise KeyError ("Error, value already assigned.")
        new_dict[new_value] = key
    return new_dict


def favorite_color(tvdict: dict[str, str]) -> str: 
    """A function checking which color appears most in a dict."""
    color_count: dict[str, str] = {}
    max_count: int = 0
    most_common: str = ""
    for key in tvdict:
        if tvdict[key] in color_count:
            color_count[tvdict[key]] += 1
        else:
            color_count[tvdict[key]] = 1
    for val in color_count:
        if color_count[val] > max_count:
            max_count = color_count[val]
            most_common = val 
    return most_common


def count(test: list[str]) -> dict[str, int]:
    """A counting function."""
    result: dict[str, int] = {}
    for value in test:
        if value in result:
            result[value] += 1
        else: 
            result[value] = 1
    return result