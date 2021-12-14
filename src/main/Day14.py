from main.utils.InputReader import InputReader


class Day14:

    def __init__(self, file):
        self.data = InputReader.get_data_str(file)

    def part1(self):
        template = self.data[0]
        polymer = {}
        for i in range(2, len(self.data)):
            pair, result = self.data[i].split(' -> ')
            polymer[pair] = result
        for _ in range(10):
            new_template = template[0]
            for i in range(len(template) - 1):
                pair = template[i: i + 2]
                insertion = polymer[pair]
                new_template += (insertion + pair[1])
            template = new_template
        to_consider = set(template)
        consider = to_consider.pop()
        min_count = template.count(consider)
        max_count = template.count(consider)
        while len(to_consider) > 0:
            count = template.count(to_consider.pop())
            min_count = min(min_count, count)
            max_count = max(max_count, count)
        return max_count - min_count

    def part2(self):
        template = self.data[0]
        polymer = {}
        for i in range(2, len(self.data)):
            pair, result = self.data[i].split(' -> ')
            polymer[pair] = result
        pairs = {}
        for i in range(len(template) - 1):
            pair = template[i: i + 2]
            if pair not in pairs:
                pairs[pair] = 1
            else:
                pairs[pair] += 1
        for _ in range(40):
            new_pairs = {}
            for pair in pairs:
                new_pair1 = pair[0] + polymer[pair]
                new_pair2 = polymer[pair] + pair[1]
                if new_pair1 not in new_pairs:
                    new_pairs[new_pair1] = pairs[pair]
                else:
                    new_pairs[new_pair1] += pairs[pair]
                if new_pair2 not in new_pairs:
                    new_pairs[new_pair2] = pairs[pair]
                else:
                    new_pairs[new_pair2] += pairs[pair]
            pairs = new_pairs
        options = ''
        for pair in pairs.keys():
            options += pair
        to_consider = set(options)
        min_count = 999999999999999999999999999999999999999999999999999999999999999999999999
        max_count = 0
        while len(to_consider) > 0:
            considering = to_consider.pop()
            count = 0
            for k, v in pairs.items():
                if considering == template[0]:
                    if considering == k[0]:
                        count += v
                else:
                    if considering == k[1]:
                        count += v
            min_count = min(min_count, count)
            max_count = max(max_count, count)
        return max_count - min_count


if __name__ == '__main__':
    day14 = Day14('resources/input14')
    print(day14.part1())
    day14 = Day14('resources/input14')
    print(day14.part2())
