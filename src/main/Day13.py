from main.utils.InputReader import InputReader


class Day13:

    def __init__(self, file):
        self.data = InputReader.get_data_str(file)
        self.grid = []
        self.folds = []

    def part1(self):
        self.prepare_data()
        self.fold(self.folds[0][0], int(self.folds[0][1]))
        return self.count_grid()

    def part2(self):
        self.prepare_data()
        for fold in self.folds:
            self.fold(fold[0], int(fold[1]))
        for line in self.grid:
            print(''.join(line))

    def prepare_data(self):
        self.folds = []
        dots = []
        for line in self.data:
            if line != '':
                if line.startswith('fold along'):
                    fold = line.split('fold along ')[1]
                    direction, value = fold.split('=')
                    self.folds.append([direction, value])
                else:
                    dots.append(line)
        x_values = []
        y_values = []
        for dot in dots:
            y, x = dot.split(',')
            x_values.append(int(x))
            y_values.append(int(y))
        max_x = max(x_values) + 1
        max_y = max(y_values) + 1
        self.grid = [['.'] * max_y for _ in range(max_x)]
        for i in range(len(x_values)):
            self.grid[x_values[i]][y_values[i]] = '#'

    def fold(self, direction, value):
        new_grid = []
        if direction == 'x':
            for i in range(len(self.grid)):
                new_line = []
                for j in range(value):
                    new_line.append(self.overlay(self.grid[i][j], self.grid[i][(2 * value) - j]))
                new_grid.append(new_line)
            self.grid = new_grid
        else:
            self.transpose()
            self.fold('x', value)
            self.transpose()

    def overlay(self, first, second):
        if first == '#' or second == '#':
            return '#'
        return '.'

    def transpose(self):
        new_grid = []
        for i in range(len(self.grid[0])):
            new_line = []
            for j in range(len(self.grid)):
                new_line.append(self.grid[j][i])
            new_grid.append(new_line)
        self.grid = new_grid

    def count_grid(self):
        count = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == '#':
                    count += 1
        return count


if __name__ == '__main__':
    day13 = Day13('resources/input13')
    print(day13.part1())
    day13.part2()
