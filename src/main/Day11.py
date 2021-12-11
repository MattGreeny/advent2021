from main.InputReader import InputReader


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
                    if self.data[i][j] > 9 and (i, j) not in self.flashed:
                        self.flash(i, j)
            for i, j in self.flashed:
                self.data[i][j] = 0
                self.flashes += 1
            self.flashed = []
        return self.flashes

    def part2(self):
        for num in range(1000):
            for i in range(len(self.data)):
                for j in range(len(self.data[0])):
                    self.data[i][j] += 1
                    if self.data[i][j] > 9 and (i, j) not in self.flashed:
                        self.flash(i, j)
            if len(self.flashed) == len(self.data) * len(self.data[0]):
                return num + 1
            for i, j in self.flashed:
                self.data[i][j] = 0
            self.flashed = []

    def flash(self, x, y):
        self.flashed.append((x, y))
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not (i == 0 and j == 0):
                    a = x + i
                    b = y + j
                    if self.is_in_range(a, b):
                        self.data[a][b] += 1
                        if self.data[a][b] > 9 and (a, b) not in self.flashed:
                            self.flash(a, b)

    def is_in_range(self, x, y):
        return 0 <= x < len(self.data) and 0 <= y < len(self.data[0])


if __name__ == '__main__':
    day11 = Day11('resources/input11')
    print(day11.part1())
    day11 = Day11('resources/input11')
    print(day11.part2())
