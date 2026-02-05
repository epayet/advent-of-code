import pytest

from twentytwentyfive.day3 import get_joltage, get_max_joltage, get_max_joltage_v2, get_max_digit


def test_joltage():
    text = """987654321111111
811111111111119
234234234234278
818181911112111"""

    assert get_joltage(text) == 357
    assert get_joltage(text, v2=True) == 3121910778619


@pytest.mark.parametrize("bank, expected_max_joltage", [
    ["987654321111111", 98],
    ["811111111111119", 89],
    ["234234234234278", 78],
    ["818181911112111", 92],
    ["97986", 99],
])
def test_get_max_joltage(bank, expected_max_joltage):
    assert get_max_joltage(bank) == expected_max_joltage


@pytest.mark.parametrize("bank, expected_max_joltage", [
    ["987654321111111", 987654321111],
    ["811111111111119", 811111111119],
    ["234234234234278", 434234234278],
    ["818181911112111", 888911112111],
])
def test_get_max_joltage_v2(bank, expected_max_joltage):
    assert get_max_joltage_v2(bank) == expected_max_joltage


def test_get_max_digit():
    assert get_max_digit("1239", 0, 2) == (2, 3)
    assert get_max_digit("1239", 0, 3) == (1, 2)
    assert get_max_digit("3129", 0, 3) == (0, 3)
    assert get_max_digit("3129", 1, 3) == (1, 1)
    assert get_max_digit("3129", 1, 2) == (2, 2)
    assert get_max_digit("3129", 3, 1) == (3, 9)
    # gaps
    assert get_max_digit("911212", 0, 3) == (0, 9)
    assert get_max_digit("911212", 1, 2) == (3, 2)
    assert get_max_digit("911212", 4, 1) == (5, 2)
