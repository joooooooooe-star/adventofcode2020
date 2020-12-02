import itertools
import functools
import operator


def get_input(file_path: str) -> list:
    with open(file_path) as f:
        return [int(line) for line in f.readlines()]


def get_winning_combo(data: list, target: int, size: int) -> tuple:

    combos = itertools.combinations(data, size)
    for combo in combos:
        if sum(combo) == target:
            return combo
    pass


if __name__ == '__main__':

    TARGET_SUM = 2020
    FILE_PATH = 'input.txt'
    SIZE = 3

    my_data = get_input(FILE_PATH)
    pair = get_winning_combo(my_data, TARGET_SUM, SIZE)

    if pair:
        print(functools.reduce(operator.mul, pair))
    else:
        print('No combos found')
