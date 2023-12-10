def day3(data):
    tab_data = make_tab_data(data)
    numbers_to_use = []
    for i, line in enumerate(tab_data):
        if i == 0:
            previous_line = None
        else:
            previous_line = tab_data[i-1]
        if i == len(tab_data) - 1:
            next_line = None
        else:
            next_line = tab_data[i+1]
        numbers_next_to_symbols = get_numbers_next_to_symbols(previous_line, line, next_line)
        numbers_to_use.extend(numbers_next_to_symbols)

    return sum(numbers_to_use)


def make_tab_data(data):
    lines = data.split("\n")
    tab_data = []
    for line in lines:
        tab_line = []
        for char in line:
            tab_line.append(char)
        tab_data.append(tab_line)
    return tab_data


def get_numbers_next_to_symbols(previous_line, line, next_line):
    valid_numbers = []
    current_number = ""
    len_line = len(line)
    for i, char in enumerate(line):
        # make / continue the number
        if char.isdigit():
            current_number += char
            # continue the number if next digit is number (and not the end of the line)
            if i < len_line-1 and line[i+1].isdigit():
                continue

        if current_number == "":
            continue

        use_number = False
        len_number = len(current_number)
        if i - len_number > -1:
            previous_char = line[i - len_number]
            if previous_char != ".":
                use_number = True
        if i < len_line - 2:
            next_char = line[i + 1]
            if next_char != ".":
                use_number = True
        if not use_number:
            use_number = check_line_should_use_number(len_number, i, previous_line)
        if not use_number:
            use_number = check_line_should_use_number(len_number, i, next_line)
        if use_number:
            valid_numbers.append(int(current_number))
        current_number = ""
    return valid_numbers


def check_line_should_use_number(len_number, i, other_line):
    if other_line is None:
        return False

    len_line = len(other_line)
    # check at least numbers below of the same size
    next_line_chars_to_check = [i - j for j in range(len_number)]
    # check the char after if not the end of the line
    if i < len_line - 2:
        next_line_chars_to_check.append(i + 1)
    # check the char before if not before the beginning of the line
    if i - len_number > -1:
        next_line_chars_to_check.append(i - len_number)
    for next_line_char_to_check in next_line_chars_to_check:
        next_char = other_line[next_line_char_to_check]
        if not next_char.isdigit() and next_char != ".":
            return True
    return False


def day3_part2(data):
    tab_data = make_tab_data(data)

    numbers_to_use = []
    for i, line in enumerate(tab_data):
        if i == 0:
            previous_line = None
        else:
            previous_line = tab_data[i - 1]
        if i == len(tab_data) - 1:
            next_line = None
        else:
            next_line = tab_data[i + 1]
        for j, char in enumerate(line):
            if char != "*":
                continue
            part_numbers = get_gear_part_numbers(previous_line, line, next_line, j)
            if len(part_numbers) == 2:
                numbers_to_use.append(part_numbers[0]*part_numbers[1])

    return sum(numbers_to_use)


def get_gear_part_numbers(previous_line, line, next_line, i):
    part_numbers = []

    check_previous = i - 1 > -1
    if check_previous:
        previous_char = line[i - 1]
        if previous_char.isdigit():
            part_numbers.append(get_number(line, i-1))
    check_next = i + 1 < len(line)
    if check_next:
        next_char = line[i+1]
        if next_char.isdigit():
            part_numbers.append(get_number(line, i+1))
    # I'm tired
    if next_line:
        # if before is number, take it
        is_previous_number = False
        if check_previous and next_line[i-1].isdigit():
            part_numbers.append(get_number(next_line, i-1))
            is_previous_number = True
        # if no number before and middle is number, take it
        if not is_previous_number and next_line[i].isdigit():
            part_numbers.append(get_number(next_line, i))
        # if no number in middle and next is number, take it
        if check_next and not next_line[i].isdigit() and next_line[i+1].isdigit():
            part_numbers.append(get_number(next_line, i+1))
    # I'm tired, copypasta
    if previous_line:
        # if before is number, take it
        is_previous_number = False
        if check_previous and previous_line[i - 1].isdigit():
            part_numbers.append(get_number(previous_line, i - 1))
            is_previous_number = True
        # if no number before and middle is number, take it
        if not is_previous_number and previous_line[i].isdigit():
            part_numbers.append(get_number(previous_line, i))
        # if no number in middle and next is number, take it
        if check_next and not previous_line[i].isdigit() and previous_line[i + 1].isdigit():
            part_numbers.append(get_number(previous_line, i + 1))

    return part_numbers


def get_number(line, i):
    beginning = get_beginning_of_number(line, i)
    number = line[beginning]
    j = beginning
    while True:
        if j + 1 == len(line) or not line[j+1].isdigit():
            return int(number)
        j += 1
        number += line[j]



def get_beginning_of_number(line, i):
    beginning = i
    while True:
        if beginning - 1 == -1:
            return beginning
        if line[beginning - 1].isdigit():
            beginning -= 1
        else:
            return beginning
