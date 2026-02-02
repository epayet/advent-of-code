import pytest

from twentytwentyfive.day2 import process_day2, get_ranges, is_invalid_id, is_invalid_id2, is_pattern_repeated


def test_day2():
    text = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

    assert process_day2(text) == 1227775554


def test_get_ranges():
    assert get_ranges("11-22,95-115") == [(11,22), (95,115)]


@pytest.mark.parametrize("number, is_invalid", (
    (1, False),
    (11, True),
    (123123, True),
    (100, False),
))
def test_is_invalid_id(number, is_invalid):
    assert is_invalid_id(number) == is_invalid


@pytest.mark.parametrize("number, is_invalid", (
    (1, False),
    (11, True),
    (123123, True),
    (100, False),
    (123123123, True),
    (1212121212, True),
    (1111111, True),
))
def test_is_invalid_id2(number, is_invalid):
    """
    12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times), and 1111111 (1 seven times) are all invalid IDs.
    """
    assert is_invalid_id2(number) == is_invalid


@pytest.mark.parametrize("pattern, number_txt, is_repeated", (
    ["1", "11", True],
    ["1", "111", True],
    ["11", "111", False],
    ["123", "123123", True],
    ["123", "123123123", True],
))
def test_is_pattern_repeated(pattern, number_txt, is_repeated):
    assert is_pattern_repeated(pattern, number_txt) == is_repeated
