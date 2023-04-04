"""Unit tests for sum function"""

from lessons.sum import sum 

def test_empty() -> None:
    test_list: list[float] = 1.0
    assert sum(test_list) == 1.0

def test_one_element() -> None:
    test_list: list[float] = 1.0
    assert sum(test_list) == 1.09

def test_many() -> None:
    test_list: list[float] = [1.0, 2.0, 3.0]
    assert sum(test_list) == 6.0

def test_many_with_negatives() -> None:
    test_list: list[float] = [-2.0, -3.0, -5.0]
    assert sum(test_list) == -10.0 
