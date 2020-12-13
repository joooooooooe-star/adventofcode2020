from collections import deque
import operator
import functools

def get_input(file_path: str) -> list:
    with open(file_path) as f:
        return [text.strip() for text in f.readlines() if text is not None]


def get_time_to_wait(bus_ids: list, departure_time: int) -> int:

    time_to_wait = 0
    while True:
        is_divisible = [bus for bus in bus_ids if departure_time % bus == 0]
        if any(is_divisible):
            print(is_divisible)
            print(departure_time)
            return (is_divisible[0] * time_to_wait)
        time_to_wait += 1
        departure_time += 1


def earliest_bus(bus_schedule: list):

    timestamp = int(bus_schedule[0])
    bus_ids = bus_schedule[1].split(',')
    bus_ids = [int(bus_id) for bus_id in bus_ids if bus_id != "x"]

    print(bus_ids)
    print(f"Time to wait is {get_time_to_wait(bus_ids, timestamp)}")


def sequential_bus(bus_schedule: list):

    bus_ids = bus_schedule[1].split(',')

    for i, bus in enumerate(bus_ids):

        if bus != "x":
            bus_ids[i] = int(bus_ids[i])

    distances = {num: distance for distance, num in enumerate(bus_ids) if type(num) == int}

    points = deque(list(distances.keys()))
    current_point = points.popleft()
    multiple = current_point
    exhausted_points = [current_point]

    while points:
        exhausted_points.append(points.popleft())
        while True:
            checks = [(current_point + distances[point]) % point == 0 for point in exhausted_points]
            if all(checks):
                multiple = functools.reduce(operator.mul, exhausted_points)
                break
            else:
                current_point += multiple

    return current_point


if __name__ == "__main__":

    FILE_PATH = "input.txt"
    bus_schedule = get_input(FILE_PATH)

    # bus_schedule = ["h", "1789,37,47,1889"]
    print(sequential_bus(bus_schedule))
