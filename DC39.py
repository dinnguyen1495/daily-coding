# Daily Coding 39
# Conway's Game of Life takes place on an infinite two-dimensional board of square cells. Each cell
# is either dead or alive, and at each tick, the following rules apply:
#     Any live cell with less than two live neighbours dies.
#     Any live cell with two or three live neighbours remains living.
#     Any live cell with more than three live neighbours dies.
#     Any dead cell with exactly three live neighbours becomes a live cell.
# A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.
# Implement Conway's Game of Life. It should be able to be initialized with a starting list of live
# cell coordinates and the number of steps it should run for. Once initialized, it should print out
# the board state at each step. Since it's an infinite board, print out only the relevant
# coordinates, i.e. from the top-leftmost live cell to bottom-rightmost live cell.
# You can represent a live cell with an asterisk (*) and a dead cell with a dot (.)

class GameOfLife:
    def __init__(self, live_cells, view_height, view_width):
        self.live_cells = sorted(live_cells)
        self.view_height = view_height
        self.view_width = view_width

    def current_board_size(self):
        max_height, max_width = 0, 0
        for live_cell in self.live_cells:
            if live_cell[0] > max_height:
                max_height = live_cell[0]
            if live_cell[1] > max_width:
                max_width = live_cell[1]
        return max_height, max_width

    def print_board(self, step, view_height, view_width):
        print('Step ' + str(step) + ':\n\tLive cells:', self.live_cells)
        width, height = self.current_board_size()
        board = []
        for x in range(view_height + 1):
            row = []
            for y in range(view_width + 1):
                if (x, y) in self.live_cells:
                    row.append('*')
                else:
                    row.append('.')
            board.append(row)
        print('\tBoard:')
        for row in board:
            print('\t' + str(row))
        print()
    
    def cell_count_neighbours(self, cell):
        live_neighbours = 0
        x, y = cell
        possible_directions = [(x - 1, y), (x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x + 1, y), (x + 1, y + 1), (x, y + 1), (x - 1, y + 1)]
        for direction in possible_directions:
            if direction in self.live_cells:
                live_neighbours += 1
        return live_neighbours
    
    def live_cell_behavior(self, live_cell, remove_list):
        count = self.cell_count_neighbours(live_cell)
        if count < 2 or count > 3:
            remove_list.append(live_cell)
            self.live_cells.sort()

    def dead_cell_behavior(self, dead_cell, temp):
        count = self.cell_count_neighbours(dead_cell)
        if count == 3:
            temp.append(dead_cell)

    def run(self, steps):
        for i in range(steps + 1):
            self.print_board(i, self.view_height, self.view_width)
            remove_list = []
            append_list = []
            for live_cell in self.live_cells:
                self.live_cell_behavior(live_cell, remove_list)
            height, width = self.current_board_size()
            for i in range(height + 2):
                for j in range(width + 2):
                    if (i, j) not in self.live_cells:
                        self.dead_cell_behavior((i, j), append_list)
            for cell in remove_list:
                self.live_cells.remove(cell)
            self.live_cells += append_list
            self.live_cells.sort()

def main():
    game = GameOfLife([(0, 1), (1, 0), (0, 0), (4, 3), (4, 2), (3, 3)], 8, 8)
    game.run(6)

if __name__ == '__main__':
    main()