import functools
import operator


def get_input(file_path: str) -> list:
    with open(file_path) as f:
        return [int(text) for text in f.readlines() if text is not None]


def get_jolt_diffs(node_dict: dict) -> dict:

    volt_checker = [1, 3]
    res = {volt: 0 for volt in volt_checker}

    for node in node_dict.keys():
        for volt in volt_checker:
            if node + volt in node_dict[node]:
                res[volt] += 1
                break

    return res


def build_node_list(adapter_set: set) -> dict:

    jolt_diff_range = range(1, 4)

    def build_destination_list(adapter: int, comp_set: set) -> list:

        test_set = set([adapter + jolt_diff for jolt_diff in jolt_diff_range])
        destinations = list(test_set.intersection(comp_set))
        destinations.sort()
        return destinations

    node_list = {adapter: build_destination_list(adapter, adapter_set) for adapter in adapter_set}

    return node_list


def count_all_paths(node_dict: dict, start_node: int, history: dict) -> (int, dict):

    my_sum = 0
    for node in node_dict[start_node]:
        if node in history.keys():
            my_sum += history[node]
        else:
            res, history = count_all_paths(node_dict, node, history)
            my_sum += res
    if len(node_dict[start_node]) > 1:
        history[start_node] = my_sum
    return my_sum, history


if __name__ == '__main__':

    # GET INPUT
    FILE_PATH = 'input.txt'
    num_list = get_input(FILE_PATH)
    num_set = set(num_list)

    # BUILT IN
    num_set.add(0)
    num_set.add(max(num_set)+3)
    last_volt = max(num_set)+3

    # BUILD TABLE
    my_node_dict = build_node_list(num_set)

    # FIND VOLT DIFFS
    ret = get_jolt_diffs(my_node_dict)
    prod = functools.reduce(operator.mul, ret.values())
    print(f'The product of the 1-jolt differences and 3-jolt differences is {prod}.')

    # FIND ALL BRANCHES
    destination = max(my_node_dict.keys())
    my_history = {destination: 1}
    all_branches, _ = count_all_paths(my_node_dict, 0, my_history)
    print(f'There are {all_branches} branches.')
