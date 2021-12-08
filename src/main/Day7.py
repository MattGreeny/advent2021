from main.InputReader import InputReader


class Day7:

    def __init__(self, file):
        self.data = InputReader.get_data_str(file)

    def part1(self):
        min_fuel = 9999999999999999
        positions = [int(x) for x in self.data[0].split(',')]
        for i in range(min(positions), max(positions) + 1):
            subtotal = 0
            for position in positions:
                subtotal += abs(position - i)
            min_fuel = min(min_fuel, subtotal)
        return min_fuel

    def part2(self):
        min_fuel = 9999999999999999
        positions = [int(x) for x in self.data[0].split(',')]
        for i in range(min(positions), max(positions) + 1):
            subtotal = 0
            for position in positions:
                x = abs(position - i)
                subtotal += (x / 2) * (x + 1)
            min_fuel = min(min_fuel, subtotal)
        return min_fuel


if __name__ == '__main__':
    day7 = Day7('resources/input7')
    print(day7.part1())
    print(day7.part2())
