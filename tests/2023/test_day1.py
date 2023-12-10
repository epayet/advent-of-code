from advent.twentythree.day1 import get_first_number, get_second_number, solve


def test_solve():
    small_codes = ['two1nine',
                   'eightwothree',
                   'abcone2threexyz',
                   'xtwone3four',
                   '4nineeightseven2',
                   'zoneight234',
                   '7pqrstsixteen'
                   ]
    assert solve(small_codes) == 281


def test_get_first_number():
    assert get_first_number('21') == 2
    assert get_first_number('adfasdf1') == 1
    assert get_first_number('twone') == 2
    assert get_first_number('1') == 1
    assert get_first_number('oneight') == 1


def test_get_last_number():
    assert get_second_number('21') == 1
    assert get_second_number('adfasdf1') == 1
    assert get_second_number('twone') == 1
    assert get_second_number('1') == 1
    assert get_second_number('oneight') == 8
