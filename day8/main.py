import re


def get_input(file_path: str) -> list:
    with open(file_path) as f:
        return [text for text in f.readlines() if text is not None]


def nop_fn(ptr: int, val: int, acc: int) -> (int, int):
    return ptr+1, acc


def acc_fn(ptr: int, val: int, acc: int) -> (int, int):
    return ptr+1, val+acc


def jmp_fn(ptr: int, val: int, acc: int) -> (int, int):
    return ptr+val, acc


def boot_fn(instr_list: list) -> (int, bool, list):

    fn_list = {"nop": nop_fn,
               "acc": acc_fn,
               "jmp": jmp_fn}

    ptr_history = set()
    ptr = 0
    acc = 0
    max_ptr = len(instr_list)

    while ptr not in ptr_history:
        ptr_history.add(ptr)
        instr = instr_list[ptr].split(' ')
        op = instr[0].strip()
        val = int(instr[1].strip())
        ptr, acc = fn_list[op](ptr, val, acc)
        if ptr == max_ptr:
            return acc, True

    return acc, False


def terminator_finder(check_list: list) -> int:

    acc, passed = boot_fn(check_list)

    replacer = {"nop": "jmp",
                "jmp": "nop",
                "acc": "acc",
                }

    if passed:
        return acc

    for i, instr in enumerate(check_list):
        instr_check_list = check_list.copy()
        instr_check_list[i] = "".join([replacer[instr[0:3]], instr[3:]])
        acc, pass_check = boot_fn(instr_check_list)
        if pass_check:
            return acc


if __name__ == '__main__':

    FILE_PATH = 'input.txt'
    my_instr_list = get_input(FILE_PATH)

    print(f'acc is {terminator_finder(my_instr_list)}')






