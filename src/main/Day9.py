from main.utils.Grid import Grid
from main.utils.InputReader import InputReader
from main.utils.Point import Point


class Day9:

    def __init__(self, file):
        self.data = InputReader.get_data_int_list(file)
        self.grid = self.initialise_grid()
        self.low_points = []
        self.considered = []
        self.in_basin = set([])

    def initialise_grid(self):
        map = {}
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data[0])):
                map[Point(i, j)] = self.data[i][j]
        return Grid(map, len(self.data[0]), len(self.data))

    def part1(self):
        for point in self.grid.map.keys():
            if self.is_low(point):
                self.low_points.append(point)
        counter = 0
        for point in self.low_points:
            counter += self.grid.get_value(point) + 1
        return counter

    def is_low(self, point):
        for neighbour in self.grid.neighbours(point):
            if self.grid.get_value(neighbour) < self.grid.get_value(point):
                return False
        return True

    def part2(self):
        self.low_points = []
        self.part1()
        basin_sizes = []
        for point in self.low_points:
            self.consider_neighbours(point)
            basin_sizes.append(len(self.in_basin))
            self.in_basin = set([])
        product = 1
        max_sizes = sorted(basin_sizes, reverse=True)[0:3]
        for size in max_sizes:
            product *= size
        return product

    def consider_neighbours(self, point):
        for neighbour in self.grid.neighbours(point):
            if neighbour not in self.considered:
                self.considered.append(neighbour)
                if self.grid.get_value(neighbour) != 9:
                    self.consider_neighbours(neighbour)
                    self.in_basin.add(neighbour)


if __name__ == '__main__':
    day9 = Day9('resources/input9')
    print(day9.part1())
    print(day9.part2())
