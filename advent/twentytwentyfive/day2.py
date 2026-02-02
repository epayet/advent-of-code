def process_day2(text: str, v2=False) -> int:
    ranges = get_ranges(text)
    # could just do sum as we go rather than storing lists and summing at the end
    invalid_ids = []
    for rng in ranges:
        range_begin, range_end = rng
        for i in range(range_begin, range_end+1):
            if v2 and is_invalid_id2(i):
                invalid_ids.append(i)
            elif not v2 and is_invalid_id(i):
                invalid_ids.append(i)
    return sum(invalid_ids)


def get_ranges(text: str) -> list[tuple]:
    ranges_text = text.split(",")
    ranges = []
    for range_text in ranges_text:
        range_text_parts = range_text.split("-")
        the_range = (int(range_text_parts[0]), int(range_text_parts[1]))
        ranges.append(the_range)
    return ranges


def is_invalid_id(number: int) -> bool:
    number_str = str(number)
    if len(number_str) % 2 != 0:
        return False

    half_len_str = len(number_str) // 2
    if number_str[:half_len_str] == number_str[half_len_str:]:
        return True

    return False


def is_invalid_id2(number: int) -> bool:
    """
    12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times), and 1111111 (1 seven times) are all invalid IDs.
    """
    number_str = str(number)
    max_possible_pattern_length = len(number_str) // 2
    for i in range(1, max_possible_pattern_length + 1):
        current_pattern = number_str[:i]
        # could check if the pattern repeated * length == full number, rather than looping through pattern bits
        if is_pattern_repeated(current_pattern, number_str):
            return True

    return False


def is_pattern_repeated(pattern: str, number_str: str) -> bool:
    pattern_length = len(pattern)
    current_pattern_index = 0
    while True:
        current_pattern_index += pattern_length
        if current_pattern_index == len(number_str):
            return True

        if number_str[current_pattern_index:current_pattern_index + pattern_length] != pattern:
            return False
