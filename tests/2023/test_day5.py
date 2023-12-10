from twentythree.day5 import day5, parse_data, get_destination, RangeNode, create_ranges_tree

base_data = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


def test_day5():
    assert day5(base_data) == 35
    assert day5(base_data, ranges=True) == 46


def test_parse_data():
    seeds, maps, destinations = parse_data(base_data)
    assert seeds == [79, 14, 55, 13]
    assert destinations == ["soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]
    assert maps["soil"] == [
        {"source": 50, "range": 48, "destination": 52},
        {"source": 98, "range": 2, "destination": 50},
    ]


def test_get_destination():
    destination_data = [{"source": 50, "range": 48, "destination": 52}, {"source": 98, "range": 2, "destination": 50}]
    assert get_destination(destination_data, 98) == 50
    assert get_destination(destination_data, 99) == 51
    assert get_destination(destination_data, 79) == 81
    assert get_destination(destination_data, 14) == 14
    assert get_destination(destination_data, 55) == 57
    assert get_destination(destination_data, 0) == 0
    assert get_destination(destination_data, 50) == 52
    assert get_destination(destination_data, 51) == 53
    assert get_destination(destination_data, 97) == 99


def test_create_ranges_tree():
    maps = {
        "soil": [
            {"source": 50, "range": 48, "destination": 52},  # 50-97, 52-99
            {"source": 98, "range": 2, "destination": 50},  # 98-99, 50,51
        ],
        "fertilizer": [
            {"source": 0, "range": 15, "destination": 39},  # 0-14, 39-53
            {"source": 15, "range": 37, "destination": 0},  # 15-51, 0-36
            {"source": 52, "range": 2, "destination": 37},  # 52-53, 37,38
        ],
        # "water": [
        #     {"source": 0, "range": 7, "destination": 42},  # 0-6, 42-48
        #     {"source": 7, "range": 4, "destination": 57},  # 7-10, 57-60
        #     {"source": 11, "range": 42, "destination": 0},  # 11-52, 0-41
        #     {"source": 53, "range": 8, "destination": 49},  # 53-60, 49-56
        # ],
    }
    range_nodes = create_ranges_tree(maps, destinations=["soil", "fertilizer"])
    assert range_nodes == [
        RangeNode(source=0, max_source=14, destination=39, children=[  # 0-14, 39-53
            RangeNode(source=53, max_source=60, destination=49)  # 53-60, 49-56
        ]),
        RangeNode(source=15, max_source=49, destination=0, children=[  # 15-51, 0-36
            RangeNode(source=0, max_source=6, destination=42),
            RangeNode(source=7, max_source=10, destination=57),
            RangeNode(source=11, max_source=49, destination=0),
        ]),
        RangeNode(source=37, max_source=49, destination=0, children=[  # 37-49, 0-41
        ]),
        RangeNode(source=50, max_source=97, destination=52, children=[  # 50-97, 52-99
            RangeNode(source=52, max_source=53, destination=37),  # 52-53, 37,38
            RangeNode(source=54, max_source=60, destination=49)  # 53-60, 49-56
        ]),
        RangeNode(source=98, max_source=99, destination=50, children=[  # 98-99
            RangeNode(source=15, max_source=51, destination=0),
        ]),
    ]
