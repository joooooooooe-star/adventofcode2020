import functools
import operator
import re

def get_input(file_path: str) -> list:
    with open(file_path) as f:
        all_text = f.read()
        return all_text.split('\n\n')


def passport_separator(passport_line: str) -> dict:
    passport_line = passport_line.replace('\n', ' ')
    passport_line = passport_line.strip()
    field_split = passport_line.split(' ')

    return {field.split(':')[0]: field.split(':')[1] for field in field_split}


def passport_data_validator(passport_data: dict) -> bool:

    valid_collector = [
        year_validation(passport_data['byr'], 1920, 2002),
        year_validation(passport_data['iyr'], 2010, 2020),
        year_validation(passport_data['eyr'], 2020, 2030),
        height_validation(passport_data['hgt']),
        hair_color_validation(passport_data['hcl']),
        eye_color_validation(passport_data['ecl']),
        pid_validation(passport_data['pid']),
    ]

    if False in valid_collector:
        return False
    return True


def year_validation(year: str, min_year, max_year) -> bool:
    YEAR_LIMIT = 4
    return min_year <= int(year) <= max_year and len(year) == YEAR_LIMIT


def height_validation(height: str) -> bool:
    in_pattern = re.compile(r'(\d{2})in')
    cm_pattern = re.compile(r'(\d{3})cm')

    in_check = re.search(in_pattern, height)
    if in_check:
        if 59 <= int(in_check[1]) <= 76:
            return True

    cm_check = re.search(cm_pattern, height)
    if cm_check:
        if 150 <= int(cm_check[1]) <= 193:
            return True

    return False


def hair_color_validation(color: str) -> bool:
    hair_pattern = re.compile(r'\#[0-9a-z]{6}$')
    if re.match(hair_pattern, color):
        return True
    return False


def eye_color_validation(color: str) -> bool:
    if color in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
        return True
    return False


def pid_validation(number: str) -> bool:
    pid_pattern = re.compile(r'\d{9}$')
    if re.match(pid_pattern, number):
        return True
    return False


if __name__ == '__main__':

    FILE_PATH = 'input.txt'
    passports = get_input(FILE_PATH)

    valid_pw_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    valid_count = 0

    for passport in passports:
        my_passport_data = passport_separator(passport)
        if valid_pw_fields.intersection(my_passport_data.keys()) == valid_pw_fields:
            if passport_data_validator(my_passport_data):
                valid_count += 1

    print(valid_count)
