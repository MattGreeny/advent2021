from main.InputReader import InputReader


class Day9:

    def __init__(self, file):
        self.data = InputReader.get_data_int_list(file)
        self.low_points = []
        self.considered = []
        self.in_basin = set([])

    def part1(self):
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data[0])):
                if self.is_low(i, j):
                    self.low_points.append((i, j))
        counter = 0
        for x, y in self.low_points:
            counter += self.data[x][y] + 1
        return counter

    def is_low(self, x, y):
        to_consider = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        for (a, b) in to_consider:
            if self.is_in_range(a, b):
                if self.data[a][b] < self.data[x][y]:
                    return False
        return True

    def is_in_range(self, x, y):
        return 0 <= x < len(self.data) and 0 <= y < len(self.data[0])

    def part2(self):
        self.low_points = []
        self.part1()
        basin_sizes = []
        for x, y in self.low_points:
            self.consider_neighbors(x, y)
            basin_sizes.append(len(self.in_basin))
            self.in_basin = set([])
        product = 1
        max_sizes = sorted(basin_sizes, reverse=True)[0:3]
        for size in max_sizes:
            product *= size
        return product

    def consider_neighbors(self, x, y):
        to_consider = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        for (a, b) in to_consider:
            if self.is_in_range(a, b) and (a, b) not in self.considered:
                self.considered.append((a, b))
                if self.data[a][b] != 9:
                    self.consider_neighbors(a, b)
                    self.in_basin.add((a, b))


if __name__ == '__main__':
    day9 = Day9('resources/input9')
    print(day9.part1())
    print(day9.part2())
