import bisect
import re
from dataclasses import dataclass
from typing import List


@dataclass
class RangeNode:
    source: int
    max_source: int
    destination: int
    children: List = None


def day5(data, ranges=False):
    seeds, maps, destinations = parse_data(data)
    lowest_location = None
    is_range = False
    for seed in seeds:
        if ranges and not is_range:
            current_seed = seed
            is_range = True
            continue

        if ranges:
            print(f"doing seed {current_seed}, range: {seed}")
            seed_range = seed
            is_range = False
        else:
            seed_range = 1
            current_seed = seed
        for j in range(seed_range):
            current_position = current_seed + j
            if j % 100000 == 0:
                print(f"checking seed {current_seed}, current position: {current_position}, still {seed_range-j} to go")
            for destination in destinations:
                current_position = get_destination(maps[destination], current_position)
            if lowest_location is None or current_position < lowest_location:
                lowest_location = current_position
    return lowest_location


def parse_data(data):
    """
    seeds: 79 14 55 13

    seed-to-soil map:
    50 98 2
    52 50 48
    """
    seeds = []
    current_destination = ""
    destinations = []
    maps = {}
    map_pattern = re.compile(r"(\w+)-to-(\w+) map")
    for i, line in enumerate(data.split("\n")):
        if i == 0:
            seeds = [int(j) for j in line.split(": ")[1].split(" ")]
            continue

        if line == "":
            continue

        if "map" in line:
            match = map_pattern.search(line)
            # sort
            if current_destination:
                maps[current_destination].sort(key=lambda x: x["source"])
            current_destination = match.groups()[1]
            maps[current_destination] = []
            destinations.append(current_destination)
            continue

        destination, source, range_length = [int(i) for i in line.split(" ")]
        maps[current_destination].append({"source": source, "destination": destination, "range": range_length})

    return seeds, maps, destinations


def get_destination_via_tree(range_nodes, source):
    pass


def create_ranges_tree(maps, destinations):
    pass


def get_destination(destination_data, source):
    the_destination_data = get_relevant_destination_data_binary(destination_data, source)
    if the_destination_data:
        offset = source - the_destination_data["source"]
        return the_destination_data["destination"] + offset
    else:
        return source


def get_relevant_destination_data(destination_data, source):
    """
    destination_data: [{"source": 98, "range": 2, "destination": 50}]
    """
    for data in destination_data:
        if source >= data["source"] and source < data["source"] + data["range"]:
            return data
    return None


def get_relevant_destination_data_binary(destination_data, source):
    size = len(destination_data)

    if size == 1:
        data = destination_data[0]
        if data["source"] <= source < data["source"] + data["range"]:
            return data
        else:
            return None

    mid = int(size / 2)

    if source >= destination_data[mid]["source"]:
        return get_relevant_destination_data_binary(destination_data[mid:], source)
    return get_relevant_destination_data_binary(destination_data[:mid], source)


def get_relevant_destination_data_binary_gpt(destination_data, source):
    sources = [data["source"] for data in destination_data]
    index = bisect.bisect_left(sources, source)

    if index > 0:
        data = destination_data[index - 1]
        if source < data["source"] + data["range"]:
            return data

    return None
