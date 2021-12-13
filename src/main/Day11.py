from main.utils.Grid import Grid
from main.utils.InputReader import InputReader
from main.utils.Point import Point


class Day11:

    def __init__(self, file):
        self.data = InputReader.get_data_int_list(file)
        self.grid = self.initialise_grid()
        self.flashes = 0
        self.flashed = []

    def initialise_grid(self):
        map = {}
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data[0])):
                map[Point(i, j)] = self.data[i][j]
        return Grid(map, len(self.data[0]), len(self.data))

    def part1(self):
        for _ in range(100):
            for point in self.grid.map.keys():
                self.grid.increment_value(point)
                if self.grid.get_value(point) > 9 and point not in self.flashed:
                    self.flash(point)
            for point in self.flashed:
                self.grid.set_value(point, 0)
                self.flashes += 1
            self.flashed = []
        return self.flashes

    def part2(self):
        for num in range(1000):
            for point in self.grid.map.keys():
                self.grid.increment_value(point)
                if self.grid.get_value(point) > 9 and point not in self.flashed:
                    self.flash(point)
            if len(self.flashed) == self.grid.width * self.grid.height:
                return num + 1
            for point in self.flashed:
                self.grid.set_value(point, 0)
            self.flashed = []

    def flash(self, point):
        self.flashed.append(point)
        for neighbour in self.grid.all_neighbours(point):
            self.grid.increment_value(neighbour)
            if self.grid.get_value(neighbour) > 9 and neighbour not in self.flashed:
                self.flash(neighbour)


if __name__ == '__main__':
    day11 = Day11('resources/input11')
    print(day11.part1())
    day11 = Day11('resources/input11')
    print(day11.part2())
