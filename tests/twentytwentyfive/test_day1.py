from advent.twentytwentyfive.day1 import process_password_text


def test_example():
    input = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

    assert process_password_text(input) == 3


def test_more_than_100():
    input = """R350
L100"""

    assert process_password_text(input) == 2


def test_less_than_100():
    input = """L350
R100"""

    assert process_password_text(input) == 2
