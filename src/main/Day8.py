from main.InputReader import InputReader


class Day8:

    def __init__(self, file):
        self.data = InputReader.get_data_str(file)

    def part1(self):
        counter = 0
        for line in self.data:
            outputs = line.split(' | ')[1].split(' ')
            for output in outputs:
                if len(output) in [2, 3, 4, 7]:
                    counter += 1
        return counter

    def part2(self):
        counter = 0
        for line in self.data:
            signals = [set(x) for x in line.split(' | ')[0].split(' ')]
            outputs = [set(x) for x in line.split(' | ')[1].split(' ')]
            codes = {}
            codes[8] = set([x for x in signals if len(x) == 7][0])
            codes[7] = set([x for x in signals if len(x) == 3][0])
            codes[4] = set([x for x in signals if len(x) == 4][0])
            codes[1] = set([x for x in signals if len(x) == 2][0])
            codes[9] = set([x for x in signals if len(x) == 6 and codes[4] <= x][0])
            codes[0] = set([x for x in signals if len(x) == 6 and codes[7] <= x and not codes[9] <= x][0])
            codes[6] = set([x for x in signals if len(x) == 6 and not codes[0] <= x and not codes[9] <= x][0])
            codes[5] = set([x for x in signals if len(x) == 5 and x <= codes[6]][0])
            codes[3] = set([x for x in signals if len(x) == 5 and codes[1] <= x and not codes[5] <= x][0])
            codes[2] = set([x for x in signals if len(x) == 5 and not codes[3] <= x and not codes[5] <= x][0])
            code = ""
            for output in outputs:
                for k, v in codes.items():
                    if output <= v <= output:
                        code += str(k)
            counter += int(code)
        return counter


if __name__ == '__main__':
    day8 = Day8('resources/input8')
    print(day8.part1())
    print(day8.part2())
