from advent.twentytwentyfive.day1 import process_password_text, process_password_text_part2


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


def test_part2():
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

    assert process_password_text_part2(input) == 6


def test_part2_left():
    input = """L1000"""
    assert process_password_text_part2(input) == 10


def test_part2_right():
    input = """R1000"""
    assert process_password_text_part2(input) == 10


def test_part2_left_exact():
    input = """L50"""
    assert process_password_text_part2(input) == 1


def test_part2_right_exact():
    input = """R50"""
    assert process_password_text_part2(input) == 1


def test_part2_right_exact_back_to0():
    input = """R50
L100
R100"""
    assert process_password_text_part2(input) == 3
