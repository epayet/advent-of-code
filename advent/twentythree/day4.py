def day4(data):
    total = 0
    for card_game in data.split('\n'):
        winning_numbers, numbers = parse_card_game(card_game)
        points = calculate_points(winning_numbers, numbers)
        total += points
    return total


def parse_card_game(card_game):
    """
    Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    """
    game = card_game.split(':')[1]
    winning_numbers_str, numbers_str = game.split('|')
    winning_numbers = [int(n) for n in winning_numbers_str.split(" ") if n]
    numbers = [int(n) for n in numbers_str.split(" ") if n]
    return winning_numbers, numbers


def calculate_points(winning_numbers, numbers):
    total = 0
    for number in numbers:
        if number in winning_numbers:
            if total == 0:
                total = 1
            else:
                total *= 2
    return total


def get_matches(winning_numbers, numbers):
    total = 0
    for number in numbers:
        if number in winning_numbers:
            total += 1
    return total


def day4_part2(data):
    copies = {}
    games = data.split('\n')
    nb_games = len(games)
    for i, card_game in enumerate(games, 1):
        if i not in copies:
            copies[i] = 1
        else:
            copies[i] += 1
        winning_numbers, numbers = parse_card_game(card_game)
        matches = get_matches(winning_numbers, numbers)
        if i < nb_games:
            for _ in range(copies[i]):
                for j in range(1, matches + 1):
                    if i+j not in copies:
                        copies[i+j] = 1
                    else:
                        copies[i+j] += 1
    return sum(copies.values())
