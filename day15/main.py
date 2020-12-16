from collections import defaultdict
from collections import deque

def get_input(file_path: str) -> list:
    with open(file_path) as f:
        return [text.strip() for text in f.readlines() if text is not None]


def get_number_game_result(numbers: list, target_iter: int) -> int:

    mem = defaultdict(deque)
    for index, num in enumerate(numbers):
        mem[num].append(index+1)

    current_turn = len(numbers) + 1

    # base
    mem[0].append(current_turn)
    current_num = 0

    current_turn += 1

    while current_turn <= target_iter:
        if current_num in mem.keys() and len(mem[current_num]) > 1:
            old_num = mem[current_num].popleft()
            current_num = mem[current_num][0] - old_num
        else:
            current_num = 0
        mem[current_num].append(current_turn)
        # print(f'turn: {current_turn}, num: {current_num}')
        current_turn += 1
    return current_num


if __name__ == "__main__":

    #FILE_PATH = "input.txt"
    #my_input = get_input(FILE_PATH)

    my_input = ["6,19,0,5,7,13,1"]
    start_numbers = [int(n) for n in my_input[0].split(",")]
    print(f'{get_number_game_result(start_numbers, 30000000)}')

