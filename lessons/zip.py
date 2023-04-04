"""Challenge Question: dictionaries. """
__author__ = "7304806767"

#make a dictionary using loops 


def zip(sum_num_list: list = list[int], some_name_list: list = list[str]) -> dict[str, int]:
    if len(sum_num_list) != len(some_name_list):
        return {}
    if len(sum_num_list) == 0 or len(some_name_list) == 0:
        return {}
    fresh_dict: dict[str, int] = {}
    for elem in range(len(sum_num_list)): 
        fresh_dict[sum_num_list[elem]] = some_name_list[elem]
    return(fresh_dict)