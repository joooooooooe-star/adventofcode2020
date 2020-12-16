from collections import defaultdict
import re
import functools
import operator

def get_input(file_path: str) -> list:
    with open(file_path) as f:
        all_text = f.read()
        return all_text.split('\n\n')


def get_conditions(conditions: list) -> list:

    conditions = conditions.split('\n')
    range_finder = re.compile(r'(\d{1,3})\-(\d{1,3})')
    conditional_ranges = list()
    for line in conditions:
        possible_ranges = [range(int(tup[0]), int(tup[1])+1) for tup in range_finder.findall(line)]
        conditional_ranges.append(possible_ranges)

    return conditional_ranges


def get_ticket_error_rate(tickets: list, conditional_check: list) -> (int, list):

    invalid_nums = list()
    invalid_tickets = list()

    for i, ticket in enumerate(tickets):
        nums = [int(n) for n in ticket.split(',') if n is not None]
        for num in nums:
            truth = [num in condition[0] or num in condition[1] for condition in conditional_check]
            if not any(truth):
                invalid_nums.append(num)
                invalid_tickets.append(i)

    return sum(invalid_nums), invalid_tickets


def find_fields(tickets: list, invalid_tickets: list) -> dict:

    field = defaultdict(list)
    for i, ticket in enumerate(tickets):
        if i not in invalid_tickets:
            nums = [int(n) for n in ticket.split(',') if n is not None]
            for j, num in enumerate(nums):
                field[j].append(num)

    return field


def check_possible_matching_conditions(fields: list, conditions: list) -> dict:

    possible_conditions = defaultdict(list)
    for field in fields.keys():
        nums = fields[field]
        for j, condition in enumerate(conditions):
            truth = [num in condition[0] or num in condition[1] for num in nums]
            if all(truth):
                possible_conditions[j].append(field)

    conditional_map = dict()

    while possible_conditions:
        remove_nums = list()
        remove_key = list()
        for key in possible_conditions.keys():
            if len(possible_conditions[key]) == 1:
                val = possible_conditions[key][0]
                conditional_map[key] = val
                remove_nums.append(val)
                remove_key.append(key)
        for key in remove_key:
            del possible_conditions[key]
        for num in remove_nums:
            for key in possible_conditions.keys():
                if num in possible_conditions[key]:
                    possible_conditions[key].remove(num)

    return conditional_map


def process_your_ticket(ticket: list, conditions: list, conditional_map: dict) -> int:

    conditions = conditions.split('\n')
    contains_departure = [i for i, cond in enumerate(conditions) if "departure" in cond]

    nums = [ticket[conditional_map[field_index]] for field_index in contains_departure]

    return functools.reduce(operator.mul, nums)


if __name__ == "__main__":

    FILE_PATH = "input.txt"
    my_input = get_input(FILE_PATH)

    my_conditions = get_conditions(my_input[0])

    nearby_tickets = my_input[2].split('\n')
    nearby_tickets = nearby_tickets[1:-1]
    ticket_error_rate, invalid_tickets = get_ticket_error_rate(nearby_tickets, my_conditions)

    split_fields = find_fields(nearby_tickets, invalid_tickets)
    all_dict = check_possible_matching_conditions(split_fields, my_conditions)

    your_ticket = my_input[1].split('\n')
    your_ticket = your_ticket[1]
    your_ticket = [int(num) for num in your_ticket.split(',')]

    print(f'multiplied nums is {process_your_ticket(your_ticket, my_input[0], all_dict)}')
    #print(f'sum of invalids is {ticket_error_rate}.')






