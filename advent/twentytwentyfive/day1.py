def process_password_text(input: str) -> int:
    rotations = input.split("\n")
    curr = 50
    nb_zero = 0
    for rotation in rotations:
        direction = rotation[0]
        amount = int(rotation[1:])
        if direction == "L":
            curr = (curr - amount) % 100
        elif direction == "R":
            curr = (curr + amount) % 100

        if curr == 0:
            nb_zero += 1
    return nb_zero


def process_password_text_part2(input: str) -> int:
    rotations = input.split("\n")
    curr = 50
    nb_zero = 0
    for rotation in rotations:
        direction = rotation[0]
        amount = int(rotation[1:])
        if direction == "L":
            if curr - amount <= 0:
                nb_zero += abs(curr - amount) // 100
                # this is to know if we crossed 0 or not. it doesn't happen if we were already at 0
                # note that this is left specific as on the right getting to 100 puts us back to 0
                if curr > 0:
                    nb_zero += 1
            curr = (curr - amount) % 100
        elif direction == "R":
            if curr + amount >= 100:
                nb_zero += (curr + amount) // 100
            curr = (curr + amount) % 100
    return nb_zero
