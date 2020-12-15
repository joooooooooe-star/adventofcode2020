import itertools
from collections import defaultdict

class Decoder:

    def __init__(self):
        self.mask: (int, int) = (0, 0, 0)
        self.memory = defaultdict(int)
        self.memory_masks = []

    def process_line(self, processes: list, op_code: int):
        for process in processes:
            splitting = process.split(' = ')
            line_type = splitting[0]
            val = splitting[1]
            if line_type == "mask":
                self.make_new_mask(val)
                if op_code == 2:
                    self.make_memory_masks(val)
            elif op_code == 1:
                self.process_mem(line_type, val)
            elif op_code == 2:
                self.process_mem_v2(line_type, val)
            else:
                print("there's an error")
                break

    def make_new_mask(self, mask: str):
        convert_ones = int(mask.replace("X", "0"), 2)
        convert_zeroes = int(mask.replace("X", "1"), 2)
        convert_x = int(mask.replace("0", "1").replace("X", "0"), 2)
        self.mask = (convert_ones, convert_zeroes, convert_x)

    def process_mem(self, line_type: str, val: str):
        mem_loc = line_type[4:-1]
        new_val = int(val)
        new_val = max([new_val, self.mask[0]]) | min([new_val, self.mask[0]])
        new_val = max([new_val, self.mask[1]]) & min([new_val, self.mask[1]])
        self.memory[mem_loc] = new_val

    def process_mem_v2(self, line_type: str, val: str):
        init_mem_loc = int(line_type[4:-1])
        init_mem_loc = self.apply_mask(init_mem_loc)
        all_locs = [init_mem_loc | memory_mask for memory_mask in self.memory_masks]
        all_locs.append(init_mem_loc)
        for loc in all_locs:
            self.memory[loc] = int(val)


    def apply_mask(self, val: int) -> int:

        new_val = val
        new_val = max([new_val, self.mask[0]]) | min([new_val, self.mask[0]])
        new_val = new_val & self.mask[2]
        return new_val

    def make_memory_masks(self, val: str):
        isolate_x = val.replace("1", "0")
        x_loc = []
        for i, ch in enumerate(isolate_x):
            if ch == "X":
                temp_str = isolate_x.replace("X", "0")
                x_loc.append("".join([temp_str[:i], "1", temp_str[(i+1):]]))

        num_convert = [int(loc, 2) for loc in x_loc]
        max_combo = len(num_convert) + 1
        all_nums = []

        for combo_length in range(1, max_combo):
            combo_list = list(itertools.combinations(num_convert, combo_length))
            combo_nums = []
            for tup in combo_list:
                combo_nums.append(sum(tup))
            all_nums.extend(combo_nums)

        self.memory_masks = all_nums


def get_input(file_path: str) -> list:
    with open(file_path) as f:
        return [text.strip() for text in f.readlines() if text is not None]


if __name__ == "__main__":

    FILE_PATH = "input.txt"
    my_input = get_input(FILE_PATH)

    myDecoder = Decoder()
    myDecoder.process_line(my_input, 2)

    print(sum(myDecoder.memory.values()))

