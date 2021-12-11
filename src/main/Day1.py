from main.utils.InputReader import InputReader


class Day1:

    def __init__(self, file):
        self.data = InputReader.get_data_int(file)

    def part1(self):
        increases = 0
        for i in range(1, len(self.data)):
            if self.data[i] > self.data[i - 1]:
                increases += 1
        return increases

    def part2(self):
        increases = 0
        for i in range(3, len(self.data)):
            if self.data[i] + self.data[i - 1] + self.data[i - 2] > self.data[i - 1] + self.data[i - 2] + self.data[i - 3]:
                increases += 1
        return increases

    def part1_golf(self):
        return sum([1 if self.data[i] > self.data[i - 1] else 0 for i in range(1, len(self.data))])


if __name__ == '__main__':
    day1 = Day1('resources/input1')
    print(day1.part1())
    print(day1.part2())
