"""example function for unit tests"""

def sum(xs: list[float]) -> float:
    sum_total: float = 0.0
    if len(xs) == 0:
        None
    #return sum of all things 
    for idx in range (0,len(xs)):
        sum_total += xs[idx]
    return(sum_total)