import functools
import operator
import re

def get_input(file_path: str) -> list:
    with open(file_path) as f:
        return [line.strip() for line in f.readlines() if line != None]


def range_finder(code: str, low_range: int, high_range: int) -> int:

    try:
        op = code[0]
    except IndexError:
        print(f"Error with {code}")
        return None

    length = (high_range - low_range + 1) / 2
    if length != 1:
        if op == "F" or op == "L":
            high_range = high_range - length
        elif op == "B" or op == "R":
            low_range = low_range + length
        else:
            print("bad input")
        return range_finder(code[1:], low_range, high_range)

    if length == 1:
        if op == "F" or op == "L":
            return low_range
        elif op == "B" or op == "R":
            return high_range
        else:
            print("bad input")
            return None


if __name__ == '__main__':

    FILE_PATH = 'input.txt'
    seat_chart = get_input(FILE_PATH)

    seatIDs = [range_finder(id[0:7], 0, 127) * 8 + range_finder(id[7:], 0, 7) for id in seat_chart]
    print(f"Max seatID is {max(seatIDs)}")

    seatIDs.sort()
    print(seatIDs)
    for num, seatID in enumerate(seatIDs):
        if num + 1 >= len(seatIDs):
            break
        if seatIDs[num+1] - seatID != 1:
            print(f"your seat is {seatID+1}")
            break
