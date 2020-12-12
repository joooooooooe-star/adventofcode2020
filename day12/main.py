

class Ship:

    def __init__(self):

        self.pos_x = 0
        self.pos_y = 0
        self.heading = 0
        self.instructions = {
            "E": self.move_east,
            "S": self.move_south,
            "W": self.move_west,
            "N": self.move_north,
            "L": self.rotate_left,
            "R": self.rotate_right,
            "F": self.move_forward,
        }

        self.heading_tr = {
            0: self.instructions["E"],
            90: self.instructions["N"],
            180: self.instructions["W"],
            270: self.instructions["S"]
        }

    def __str__(self):
        return f'Ship at {self.pos_x}, {self.pos_y}, heading is {self.heading}'

    def run_instruction(self, instr: str):

        guide = instr[0]
        val = int(instr[1:])
        self.instructions[guide](val)

    def move_north(self, val: int):
        self.pos_y += val

    def move_east(self, val: int):
        self.pos_x += val

    def move_south(self, val: int):
        self.pos_y -= val

    def move_west(self, val: int):
        self.pos_x -= val

    def move_forward(self, val: int):
        self.heading_tr[self.heading](val)

    def rotate_left(self, val: int):
        self.heading = (self.heading + val) % 360

    def rotate_right(self, val: int):
        temp_heading = (self.heading - val)
        if temp_heading < 0:
            self.heading = temp_heading % 360
        else:
            self.heading = temp_heading

    def get_manhattan_distance(self) -> int:
        return sum([abs(self.pos_x), abs(self.pos_y)])


class WaypointShip(Ship):

    def __init__(self):
        super().__init__()
        self.wp_x = 10
        self.wp_y = 1

    def move_north(self, val: int):
        self.wp_y += val

    def move_west(self, val: int):
        self.wp_x -= val

    def move_south(self, val: int):
        self.wp_y -= val

    def move_east(self, val: int):
        self.wp_x += val

    def move_forward(self, val: int):
        self.pos_x += val * self.wp_x
        self.pos_y += val * self.wp_y

    def rotate_left(self, val: int):
        rotate_times = int(val % 360 / 90)
        for _ in range(0, rotate_times):
            temp_x = self.wp_y * -1
            temp_y = self.wp_x
            self.wp_x = temp_x
            self.wp_y = temp_y

    def rotate_right(self, val: int):
        rotate_times = int(val % 360 / 90)
        for _ in range(0, rotate_times):
            temp_x = self.wp_y
            temp_y = self.wp_x * -1
            self.wp_x = temp_x
            self.wp_y = temp_y


def get_input(file_path: str) -> list:
    with open(file_path) as f:
        return [text.strip() for text in f.readlines() if text is not None]


if __name__ == "__main__":

    FILE_PATH = "input.txt"
    my_instructions = get_input(FILE_PATH)

    my_ship = WaypointShip()
    for instruction in my_instructions:
        my_ship.run_instruction(instruction)

    print(my_ship.get_manhattan_distance())
