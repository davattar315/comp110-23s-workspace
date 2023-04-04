"""Testing Util Functions."""
__author__ = "730480676"

from exercises.ex05.utils import only_evens

from exercises.ex05.utils import concat

from exercises.ex05.utils import sub


def test_only_evens_1() -> None:
    """Only evens test 1."""
    test_list: list[float] = [1.0, 2.0, 3.0, 4.0]
    assert only_evens(test_list) == [2.0, 4.0]


def test_only_evens_2() -> None:
    """Only evens test 2."""
    test_list: list[float] = [-1.0, -2.0, -3.0, -4.0]
    assert only_evens(test_list) == [-2.0, -4.0]


def test_only_evens_3() -> None:
    """Only evens test 3."""
    test_list: list[float] = []
    assert only_evens(test_list) == []


def test_concat_1() -> None:
    """Concat test 1."""
    test_list_a: list[int] = [1, 2, 3]
    test_list_b: list[int] = [4, 5, 6]
    assert concat(test_list_a, test_list_b) == [1, 2, 3, 4, 5, 6]


def test_concat_2() -> None:
    """Concat test 2."""
    test_list_a: list[int] = [-8, -7, -4,]
    test_list_b: list[int] = [-3, -2, -1]
    assert concat(test_list_a, test_list_b) == [-8, -7, -4, -3, -2, -1]


def test_concat_3() -> None:
    """Concat test 3."""
    test_list_a: list[int] = [-1, 0, 1]
    test_list_b: list[int] = [2, 3]
    assert concat(test_list_a, test_list_b) == [-1, 0, 1, 2, 3] 


def test_sub_1() -> None:
    """Sub test 1."""
    test_list: list[int] = [1, 2, 3, 4]
    start: int = 0
    end: int = 2    
    assert sub(test_list, start, end) == [1, 2]


def test_sub_2() -> None:
    """Sub test 1."""
    test_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    start: int = 0
    end: int = 4  
    assert sub(test_list, start, end) == [1, 2, 3, 4]


def test_sub_3() -> None:
    """Sub test 1."""
    test_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    start: int = -1
    end: int = 3  
    assert sub(test_list, start, end) == [1, 2, 3]