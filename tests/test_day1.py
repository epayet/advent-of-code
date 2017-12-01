import pytest

from advent.day1 import sum_digits_match_next_digit


@pytest.mark.parametrize('value, expected', [
    ('1122', 3),
    ('1111', 4),
    ('1234', 0),
    ('91212129', 9),
])
def test_sum_digits_match_next_digit(value, expected):
    assert sum_digits_match_next_digit(value) == expected
