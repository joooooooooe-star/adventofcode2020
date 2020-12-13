import itertools
from collections import defaultdict


class SeatChart:

    def __init__(self, instructions: list):
        self.rows = [line for line in instructions]
        self.x_max = len(self.rows[0])
        self.y_max = len(self.rows)
        self.adj_cell_list = defaultdict(int)

        all_possible_coords = {-1, 0, 1}
        self.search_matrix = list(itertools.product(all_possible_coords, repeat=2))
        self.search_matrix.remove((0, 0))
        # self.find_valid_adjacent_cells()
        self.find_valid_adjacent_cells_v2()

    def __str__(self):
        return "\n".join([row for row in self.rows])

    def __eq__(self, other):
        if isinstance(other, SeatChart):
            return self.rows == other.rows
        return False

    def find_filled_adjacent_cells(self):
        for base_y in range(0, self.y_max):
            for base_x in range(0, self.x_max):
                for (coord_x, coord_y) in self.search_matrix:
                    boundary_conds = [
                        base_y + coord_y < 0,
                        base_y + coord_y >= self.y_max,
                        base_x + coord_x < 0,
                        base_x + coord_x >= self.x_max,
                    ]
                    if not any(boundary_conds) and self.rows[base_y + coord_y][base_x + coord_x] == "#":
                        self.adj_cell_list[(base_x, base_y)] += 1

    def find_first_directional_occupied(self, base_y, base_x, search_vector) -> int:

        checkpoint_y = base_y
        checkpoint_x = base_x

        while True:
            checkpoint_y += search_vector[1]
            checkpoint_x += search_vector[0]
            boundary_conds = [
                checkpoint_y < 0,
                checkpoint_y >= self.y_max,
                checkpoint_x < 0,
                checkpoint_x >= self.x_max,
            ]
            if any(boundary_conds):
                return 0
            if self.rows[checkpoint_y][checkpoint_x] == "L":
                return 0
            if self.rows[checkpoint_y][checkpoint_x] == "#":
                return 1

    def find_valid_adjacent_cells_v2(self):
        for base_y in range(0, self.y_max):
            for base_x in range(0, self.x_max):
                for vec in self.search_matrix:
                    self.adj_cell_list[(base_x, base_y)] += self.find_first_directional_occupied(
                        base_y, base_x, vec)

    def update_empty_seat(self, cell_x, cell_y, tolerance) -> str:
        if self.adj_cell_list[(cell_x, cell_y)] == 0:
            return "#"
        else:
            return "L"

    def update_occupied_seat(self, cell_x, cell_y, tolerance) -> str:
        if self.adj_cell_list[(cell_x, cell_y)] >= tolerance:
            return "L"
        else:
            return "#"

    def new_cell_state(self, tolerance):
        ops = {
            "L": self.update_empty_seat,
            "#": self.update_occupied_seat,
            ".": lambda a, b, c: "."
        }

        new_instructions = []
        for cell_y, row in enumerate(self.rows):
            this_row = "".join([ops[char](cell_x, cell_y, tolerance) for cell_x, char in enumerate(row)])
            new_instructions.append(this_row)

        return SeatChart(new_instructions)

    def seat_count(self) -> int:
        return sum([row.count("#") for row in self.rows])


def get_input(file_path: str) -> list:
    with open(file_path) as f:
        return [text.strip() for text in f.readlines() if text is not None]


if __name__ == "__main__":
    FILE_PATH = "input.txt"
    my_instructions = get_input(FILE_PATH)
    my_seat_chart = SeatChart(my_instructions)
    while my_seat_chart != my_seat_chart.new_cell_state(5):
        my_seat_chart = my_seat_chart.new_cell_state(5)

    print(my_seat_chart.seat_count())
