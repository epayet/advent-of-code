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
