from main.InputReader import InputReader


class Day2:

    def __init__(self, file):
        self.data = InputReader.get_data_str(file)

    def part1(self):
        forward = 0
        depth = 0
        for instruction in self.data:
            direction, value = instruction.split(" ")
            if direction == "forward":
                forward += int(value)
            elif direction == "down":
                depth += int(value)
            else:
                depth -= int(value)
        return forward * depth

    def part2(self):
        forward = 0
        depth = 0
        aim = 0
        for instruction in self.data:
            direction, value = instruction.split(" ")
            value = int(value)
            if direction == "forward":
                forward += value
                depth += value * aim
            elif direction == "down":
                aim += value
            else:
                aim -= value
        return forward * depth


if __name__ == '__main__':
    day2 = Day2('resources/input2')
    print(day2.part1())
    print(day2.part2())
