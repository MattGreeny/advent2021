from main.InputReader import InputReader


class DayX:

    def __init__(self, file):
        self.data = InputReader.get_data_str(file)

    def part1(self):
        return 'foo'

    def part2(self):
        return 'bar'


if __name__ == '__main__':
    dayX = DayX('resources/inputX')
    print(dayX.part1())
    print(dayX.part2())
