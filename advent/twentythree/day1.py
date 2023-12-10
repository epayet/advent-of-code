numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
letter_map = {n: i for i, n in enumerate(numbers)}
letter_map.update({str(i): i for i in range(10)})
numbers.extend(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])


def solve(codes):
    total = 0
    for code in codes:
        first_number = get_first_number(code)
        second_number = get_second_number(code)
        number = int(f"{first_number}{second_number}")
        total += number
    return total


def get_first_number(code):
    earliest = -1
    found_number = None
    for number in numbers:
        found = code.find(number)
        if found == -1:
            continue
        if earliest == -1 or found < earliest:
            earliest = found
            found_number = number
    return letter_map[found_number]


def get_second_number(code):
    latest = None
    found_number = None
    for number in numbers:
        found = code.rfind(number)
        if found == -1:
            continue
        if latest is None or found > latest:
            latest = found
            found_number = number
    return letter_map[found_number]
