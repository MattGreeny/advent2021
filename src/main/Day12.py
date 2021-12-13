from main.utils.InputReader import InputReader


class Day12:

    def __init__(self, file):
        self.data = InputReader.get_data_str(file)
        self.connections = {}
        self.number_of_paths = 0

    def part1(self):
        self.prepare_data()
        self.step(['start'])
        return self.number_of_paths

    def part2(self):
        self.prepare_data()
        self.step_part2(['start'], True)
        return self.number_of_paths

    def prepare_data(self):
        for line in self.data:
            start, finish = line.split('-')
            if start in self.connections.keys():
                self.connections[start].append(finish)
            else:
                self.connections[start] = [finish]
            if finish in self.connections.keys():
                self.connections[finish].append(start)
            else:
                self.connections[finish] = [start]

    def step(self, steps):
        last = steps[len(steps) - 1]
        if last == 'end':
            self.number_of_paths += 1
            return
        for option in self.connections[last]:
            if option.isupper() or option not in steps:
                self.step(steps + [option])

    def step_part2(self, steps, double_trip_available):
        last = steps[len(steps) - 1]
        if last == 'end':
            self.number_of_paths += 1
            return
        for option in self.connections[last]:
            if option.isupper() or option not in steps:
                self.step_part2(steps + [option], double_trip_available)
            elif double_trip_available and steps.count(option) == 1 and option != 'start':
                self.step_part2(steps + [option], False)


if __name__ == '__main__':
    day12 = Day12('resources/input12')
    print(day12.part1())
    day12 = Day12('resources/input12')
    print(day12.part2())
