from twentythree.day4 import day4, parse_card_game, calculate_points, day4_part2


def test_day_4():
    data="""Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
    assert day4(data) == 13


def test_parse_card_game():
    card_game = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    assert parse_card_game(card_game) == ([41, 48, 83, 86, 17], [83, 86,  6, 31, 17,  9, 48, 53])


def test_calculate_points():
    winning_numbers, numbers = [41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53]
    assert calculate_points(winning_numbers, numbers) == 8


def test_part2():
    data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
    assert day4_part2(data) == 30
