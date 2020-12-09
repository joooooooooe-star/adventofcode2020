
def get_input(file_path: str) -> list:
    with open(file_path) as f:
        return [line for line in f.readlines()]


def password_validity_initial(password_line: str) -> bool:
    text_split = password_line.split()

    limits = text_split[0].split("-")
    lower_limit = int(limits[0])
    upper_limit = int(limits[1])

    char_search = text_split[1][0]

    char_count = text_split[2].count(char_search)

    if lower_limit <= char_count <= upper_limit:
        return True
    else:
        return False


def password_validity_revised(pass_line: str) -> bool:

    OFFSET = 1
    text_split = pass_line.split()

    limits = text_split[0].split("-")
    first_pos = int(limits[0]) - OFFSET
    second_pos = int(limits[1]) - OFFSET

    char_search = text_split[1][0]

    total_char = sum([text_split[2][first_pos] == char_search, text_split[2][second_pos] == char_search])

    if total_char == 1:
        return True
    else:
        return False


if __name__ == '__main__':

    FILE_PATH = 'input.txt'

    my_data = get_input(FILE_PATH)
    valid_pass_count = (password_validity_revised(line) for line in my_data)

    print(f"There are {sum(valid_pass_count)} valid passwords.")

