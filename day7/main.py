import re


def get_input(file_path: str) -> list:
    with open(file_path) as f:
        return [text for text in f.readlines()]


def bag_contains_parse(statement: str) -> dict:
    statement_split = statement.split("contain")
    key_color = statement_split[0].split("bags")[0].strip()
    content = re.compile(r'(\d) (\w+ \w+) bags?')
    my_dict = {key_color: {color: int(num) for num, color in content.findall(statement_split[1])}}
    return my_dict


def find_all_bags(bag_list: dict, search_cond: list) -> list:

    new_search_cond = search_cond
    for cond in search_cond:
        for bag in bag_list:
            if cond in bag_list[bag].keys():
                new_search_cond.append(bag)
    if set(new_search_cond) == set(search_cond):
        return list(set(new_search_cond))
    else:
        return find_all_bags(bag_list, list(set(new_search_cond)))


def bag_checker(bag_list: dict, search_cond: list) -> int:

    SELF_COUNT = 1
    for cond in search_cond:
        if not bag_list[cond]:
            return 1
        else:
            all_bags = bag_list[cond].keys()
            sum_bags = [bag_checker(bag_list, [key]) * bag_list[cond][key] for key in all_bags]
            return sum(sum_bags) + SELF_COUNT


if __name__ == '__main__':

    FILE_PATH = 'input.txt'
    SELF_OFFSET = 1
    raw_bag_list = get_input(FILE_PATH)

    parsed_result = {}
    for my_bag in raw_bag_list:
        parsed_result.update(bag_contains_parse(my_bag))

    init_search_cond = ["shiny gold"]

    all_my_bags = find_all_bags(parsed_result, init_search_cond)

    print(f'total containing {init_search_cond[0]} is {len(all_my_bags) - SELF_COUNT}')

    print(f'a single {init_search_cond[0]} contains {bag_checker(parsed_result, init_search_cond) - 1} bags')
