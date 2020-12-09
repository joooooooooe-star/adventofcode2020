import functools
import operator


def get_input(file_path: str) -> list:
    with open(file_path) as f:
        return [line.strip() for line in f.readlines()]


def tree_counter(snow_map: list, directions: dict) -> int:

    x_pos = 0
    y_pos = 0
    tree_count = 0

    MAP_BORDER = len(snow_map[0])

    while y_pos < len(snow_map):
        if snow_map[y_pos][x_pos] == "#":
            tree_count += 1

        x_pos = x_pos + directions['right']

        if x_pos >= MAP_BORDER:
            x_pos -= MAP_BORDER

        y_pos = y_pos + directions['down']

    return tree_count


if __name__ == '__main__':

    FILE_PATH = 'input.txt'
    my_map = get_input(FILE_PATH)

    my_directions = [
        {'right': 1, 'down': 1},
        {'right': 3, 'down': 1},
        {'right': 5, 'down': 1},
        {'right': 7, 'down': 1},
        {'right': 1, 'down': 2},
    ]

    tree_list = [tree_counter(my_map, slope) for slope in my_directions]

    print(f'The product is {functools.reduce(operator.mul, tree_list)} trees.')
