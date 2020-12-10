from collections import deque

def get_input(file_path: str) -> list:
    with open(file_path) as f:
        return [int(text) for text in f.readlines() if text is not None]


def find_target_number(number_list: list) -> int:

    PREAMBLE_LENGTH = 25
    # init condition
    active_list = deque(number_list[0:PREAMBLE_LENGTH])
    number_list = number_list[PREAMBLE_LENGTH:]

    for num in number_list:
        active_set = set(active_list)
        for check_num in active_set:
            if num - check_num in active_set:
                found_flag = True
                break
        if found_flag == False:
            return num
        found_flag = False
        active_list.append(num)
        try:
            active_list.popleft()
        except IndexError:
            print("no more in active_list!")
            return None

    return None


def find_contigious_sum(number_list: list, target_number: int) -> int:

    ANS_WIDTH = 2
    for start_point, _ in enumerate(number_list):
        end_point = start_point + ANS_WIDTH
        check_list = number_list[start_point:end_point]
        while sum(check_list) <= target_number and end_point < len(number_list):
            if sum(check_list) == target_number:
                return min(check_list) + max(check_list)
            else:
                end_point += 1
                check_list = number_list[start_point:end_point]

    return None


if __name__ == '__main__':

    FILE_PATH = 'input.txt'
    my_num_list = get_input(FILE_PATH)
    target_num = find_target_number(my_num_list)

    print(f"sum of min max contiguous is {find_contigious_sum(my_num_list, target_num)}")







