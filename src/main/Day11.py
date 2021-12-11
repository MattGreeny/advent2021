from main.utils.InputReader import InputReader
from main.utils.Point import Point


class Day11:

    def __init__(self, file):
        self.data = InputReader.get_data_int_list(file)
        self.flashes = 0
        self.flashed = []

    def part1(self):
        for _ in range(100):
            for i in range(len(self.data)):
                for j in range(len(self.data[0])):
                    self.data[i][j] += 1
                    point = Point(i, j)
                    if self.data[i][j] > 9 and point not in self.flashed:
                        self.flash(point)
            for point in self.flashed:
                self.data[point.x][point.y] = 0
                self.flashes += 1
            self.flashed = []
        return self.flashes

    def part2(self):
        for num in range(1000):
            for i in range(len(self.data)):
                for j in range(len(self.data[0])):
                    self.data[i][j] += 1
                    point = Point(i, j)
                    if self.data[i][j] > 9 and point not in self.flashed:
                        self.flash(point)
            if len(self.flashed) == len(self.data) * len(self.data[0]):
                return num + 1
            for point in self.flashed:
                self.data[point.x][point.y] = 0
            self.flashed = []

    def flash(self, point):
        self.flashed.append(point)
        for neighbour in point.all_neighbours():
            if self.is_in_range(neighbour):
                self.data[neighbour.x][neighbour.y] += 1
                if self.data[neighbour.x][neighbour.y] > 9 and neighbour not in self.flashed:
                    self.flash(neighbour)

    def is_in_range(self, point):
        return 0 <= point.x < len(self.data) and 0 <= point.y < len(self.data[0])


if __name__ == '__main__':
    day11 = Day11('resources/input11')
    print(day11.part1())
    day11 = Day11('resources/input11')
    print(day11.part2())
