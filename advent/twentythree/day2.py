def day2(data):
    """
    which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes

    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    """
    total_valid_ids = 0
    maxs = {"red": 12, "green": 13, "blue": 14}

    for game in data.split("\n"):
        game_name, game_content = game.split(":")
        sets = game_content.split(";")
        nope = False
        for ze_set in sets:
            cubes = ze_set.split(",")
            for cube in cubes:
                _, nb_cube, cube_color = cube.split(" ")
                if int(nb_cube) > maxs[cube_color]:
                    nope = True
                    break
        if nope:
            continue
        game_id = int(game_name.split(" ")[1])
        total_valid_ids += game_id

    return total_valid_ids


def day2_part2(data):
    total_mins = 0
    for game in data.split("\n"):
        game_name, game_content = game.split(":")
        sets = game_content.split(";")
        mins = {}
        for ze_set in sets:
            cubes = ze_set.split(",")
            for cube in cubes:
                _, nb_cube, cube_color = cube.split(" ")
                if cube_color not in mins or int(nb_cube) > mins[cube_color]:
                    mins[cube_color] = int(nb_cube)
        mins_multiplied = 1
        for this_min in mins.values():
            mins_multiplied = this_min * mins_multiplied
        total_mins += mins_multiplied

    return total_mins
