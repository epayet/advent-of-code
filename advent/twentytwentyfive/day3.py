def get_joltage(text: str, v2:bool=False) -> int:
    total = 0
    for bank in text.split("\n"):
        if v2:
            total += get_max_joltage_v2(bank)
        else:
            total += get_max_joltage(bank)
    return total


def get_max_joltage(bank: str) -> int:
    """
    was good enough for part 1
    we could use the v2 with specifying max_length to 2
    """
    max_first_digit = 0
    max_first_digit_location = 0
    for i, digit in enumerate(bank[:-1]):
        int_digit = int(digit)
        if int_digit > max_first_digit:
            max_first_digit = int_digit
            max_first_digit_location = i

    max_right_digit = 0
    for right_digit in bank[max_first_digit_location+1:]:
        int_right_digit = int(right_digit)
        if int_right_digit > max_right_digit:
            max_right_digit = int_right_digit

    return int(str(max_first_digit) + str(max_right_digit))


def get_max_joltage_v2(bank: str) -> int:
    max_digit_location, max_digit = -1, 0
    max_joltage = ""
    max_length = 12
    for i in range(max_length):
        max_digit_location, max_digit = get_max_digit(bank, max_digit_location + 1, max_length - i)
        max_joltage += str(max_digit)
    return int(max_joltage)


def get_max_digit(bank, start, max_length) -> tuple[int, int]:
    max_digit_location = start
    max_digit = 0
    end = len(bank) - max_length + 1
    for i, digit in enumerate(bank[start:end]):
        int_digit = int(digit)
        if int_digit > max_digit:
            max_digit = int_digit
            max_digit_location = start + i
    return max_digit_location, max_digit
