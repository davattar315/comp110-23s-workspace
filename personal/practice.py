"""Returns a list of words that are shorter than 5 characters"""

def shrink(x: dict[str, int]) -> list[int]:
    idx = 0
    new_list: list[int] = []
    while idx < len(x):
        if idx % 2 == 0 and len(x[idx]) < 11:
            new_list.append(x[idx])
        idx += 1
    return new_list