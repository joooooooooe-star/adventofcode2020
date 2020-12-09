import functools
import operator
import re

def get_input(file_path: str) -> list:
    with open(file_path) as f:
        all_text = f.read()
        all_text = all_text.split('\n\n')
        return [text.strip() for text in all_text]


def unique_answers(answers: str) -> int:

    split_answers = [ch for ch in answers if ch != '\n']
    uniques = set(split_answers)
    return len(uniques)


def sum_same_answers(answers: str) -> int:

    individual_answers = answers.split('\n')
    total_people = len(individual_answers)
    tabbed_answers = {}
    for ans in individual_answers:
        for ch in ans:
            if ch in tabbed_answers:
                tabbed_answers[ch] += 1
            else:
                tabbed_answers[ch] = 1

    return sum([val == total_people for val in tabbed_answers.values()])


if __name__ == '__main__':

    FILE_PATH = 'input.txt'
    answer_list = get_input(FILE_PATH)

    all_uniques = [unique_answers(answer) for answer in answer_list]

    all_same = [sum_same_answers(answer) for answer in answer_list]
    print(f"the sum is {sum(all_uniques)}")
    print(f"the sum of same answers is {sum(all_same)}")

