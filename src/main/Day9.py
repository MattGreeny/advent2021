from main.utils.InputReader import InputReader
from main.utils.Point import Point


class Day9:

    def __init__(self, file):
        self.data = InputReader.get_data_int_list(file)
        self.low_points = []
        self.considered = []
        self.in_basin = set([])

    def part1(self):
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data[0])):
                point = Point(i, j)
                if self.is_low(point):
                    self.low_points.append(point)
        counter = 0
        for point in self.low_points:
            counter += self.data[point.x][point.y] + 1
        return counter

    def is_low(self, point):
        for neighbour in point.neighbours():
            if self.is_in_range(neighbour):
                if self.data[neighbour.x][neighbour.y] < self.data[point.x][point.y]:
                    return False
        return True

    def is_in_range(self, point):
        return 0 <= point.x < len(self.data) and 0 <= point.y < len(self.data[0])

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
        for neighbour in point.neighbours():
            if self.is_in_range(neighbour) and neighbour not in self.considered:
                self.considered.append(neighbour)
                if self.data[neighbour.x][neighbour.y] != 9:
                    self.consider_neighbours(neighbour)
                    self.in_basin.add(neighbour)


if __name__ == '__main__':
    day9 = Day9('resources/input9')
    print(day9.part1())
    print(day9.part2())
