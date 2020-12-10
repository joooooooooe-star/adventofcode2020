

def get_input(file_path: str) -> list:
    with open(file_path) as f:
        return [int(text) for text in f.readlines() if text is not None]


def volt_multiplier(adapter_set: set) -> dict:

    diff_memo = {1: 0, 2: 0, 3: 0}

    current_volt = 0
    while len(adapter_set) != 0:
        for volt_diff in range(1, 4):
            new_volt = current_volt + volt_diff
            if new_volt in adapter_set:
                diff_memo[volt_diff] += 1
                adapter_set.remove(new_volt)
                current_volt = new_volt
                break
    return diff_memo


def node_builder(adapter_set: set) -> dict:

    adapter_list = list(adapter_set)
    adapter_list.sort()
    node_list = dict()
    for adapter in adapter_list:
        destinations = [f+adapter for f in range(1, 4) if f+adapter in adapter_set]
        destinations.sort()
        node_list[adapter] = destinations

    return node_list


def path_counter_graph(node_dict: dict, start_node: int) -> int:

    my_sum = 0
    for node in node_dict[start_node]:
        if node in history.keys():
            my_sum += history[node]
        else:
            res = path_counter_graph(node_dict, node)
            my_sum += res
    if len(node_dict[start_node]) > 1:
        history[start_node] = my_sum
    return my_sum


if __name__ == '__main__':

    FILE_PATH = 'input.txt'
    num_list = get_input(FILE_PATH)
    num_set = set(num_list)
    num_set.add(0)

    # BUILT IN
    num_set.add(max(num_set)+3)
    last_volt = max(num_set)+3

    my_node_dict = node_builder(num_set)
    destination = max(my_node_dict.keys())
    history = {destination: 1}
    print(path_counter_graph(my_node_dict, 0))
