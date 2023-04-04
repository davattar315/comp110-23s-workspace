"""Testing Functions EX07."""
__author__ = "730480676"


from dictionary import invert
from dictionary import favorite_color 
from dictionary import count 


def test_invert() -> None:
    """Testing invert."""
    assert invert({"Jonesy": "1", "Jeron": "2", "Silly": "3"}) == {"1": "Jonesy", "2": "Jeron", "3": "Silly"}
    assert invert({"oh": "1", "nah": "2", "hillary": "3"}) == {"1": "oh", "2": "nah", "3": "hillary"}
    assert invert({}) == {}


def test_favorite_color() -> None:
    """Testing favorite_color."""
    assert favorite_color({"Bob": "blue", "Amanda": "yellow", "Josh": "blue"}) == ("blue")
    assert favorite_color({"Taylor": "green", "Mark": "green", "Slay": "teal"}) == ("green")
    assert favorite_color({}) == ""


def test_count() -> None:
    """Testing count."""
    assert count(["blue", "green", "yellow", "blue"]) == {"blue": 2, "green": 1, "yellow": 1}
    assert count(["bananna", "apple", "blueberry", "blueberry", "raspberry"]) == {"bananna": 1, "apple": 1, "blueberry": 2, "raspberry": 1}
    assert count({}) == {}