from twentythree.day3 import day3, make_tab_data, get_numbers_next_to_symbols, day3_part2, get_gear_part_numbers, \
    get_number, get_beginning_of_number


def test_day3():
    data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
    assert day3(data) == 4361


def test_make_tab_data():
    data = """467..114..
...*......"""
    tab_data = [
        ["4", "6", "7", ".", ".", "1", "1", "4", ".", "."],
        [".", ".", ".", "*", ".", ".", ".", ".", ".", "."]
    ]
    assert make_tab_data(data) == tab_data


def test_get_numbers_next_to_symbols():
    data = [
        ["4", "6", "7", ".", ".", "1", "1", "4", ".", ".", "9"],
        [".", ".", ".", "*", ".", ".", ".", ".", ".", ".", "#"],
    ]
    assert get_numbers_next_to_symbols(None, data[0], data[1]) == [467, 9]
    data = [
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "#", "."],
        ["4", "6", "7", ".", ".", "1", "1", "4", ".", ".", "9"],
        [".", ".", ".", "*", ".", ".", ".", ".", ".", ".", "."],
    ]
    assert get_numbers_next_to_symbols(data[0], data[1], data[2]) == [467, 9]
    data = [
        [".", ".", ".", "*", ".", ".", ".", ".", ".", "#", "."],
        ["4", "6", "7", ".", ".", "1", "1", "4", ".", ".", "9"],
    ]
    assert get_numbers_next_to_symbols(data[0], data[1], None) == [467, 9]
    data = [
        ["4", "6", "7", ".", "#", "1", "1", "4", ".", ".", "9"],
    ]
    assert get_numbers_next_to_symbols(None, data[0], None) == [114]


def test_day3_part2():
    data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
    assert day3_part2(data) == 467835


def test_get_gear_part_numbers():
    data = [
        [".", ".", ".", "*", "2", ".", ".", ".", "2", "#", "*"],
        ["5", "0", "0", "*", "*", "1", "1", "4", ".", "*", "9"],
        [".", ".", ".", "*", ".", ".", "*", ".", "1", "1", "."],
    ]
    assert get_gear_part_numbers(None, data[0], data[1], 3) == [2, 500]
    assert get_gear_part_numbers(None, data[0], data[1], 10) == [9]
    assert get_gear_part_numbers(data[0], data[1], data[2], 3) == [500, 2]
    assert get_gear_part_numbers(data[0], data[1], data[2], 4) == [114, 2]
    assert get_gear_part_numbers(data[0], data[1], data[2], 9) == [9, 11, 2]
    assert get_gear_part_numbers(data[1], data[2], None, 3) == [500]


def test_get_number():
    data = ["5", "0", "0", "*", "*", "1", "1", "4", ".", "*", "9"]
    assert get_number(data, 2) == 500
    assert get_number(data, 6) == 114
    assert get_number(data, 10) == 9


def test_get_beginning_of_number():
    data = ["5", "0", "0", "*", "*", "1", "1", "4", ".", "*", "9"]
    assert get_beginning_of_number(data, 0) == 0
    assert get_beginning_of_number(data, 1) == 0
    assert get_beginning_of_number(data, 2) == 0
    assert get_beginning_of_number(data, 5) == 5
    assert get_beginning_of_number(data, 6) == 5
    assert get_beginning_of_number(data, 7) == 5
    assert get_beginning_of_number(data, 10) == 10
