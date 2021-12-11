from main.utils.InputReader import InputReader


class Day6:

    def __init__(self, file):
        self.data = InputReader.get_data_str(file)

    def part1(self):
        fish = [int(x) for x in self.data[0].split(',')]
        for _ in range(80):
            new_fish = []
            for fish in fish:
                if fish == 0:
                    new_fish.append(6)
                    new_fish.append(8)
                else:
                    new_fish.append(fish - 1)
            fish = new_fish
        return len(fish)

    def part2(self):
        fish = [int(x) for x in self.data[0].split(',')]
        fish_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
        for single_fish in fish:
            fish_dict[single_fish] += 1
        for _ in range(256):
            new_fish_dict = {8: fish_dict[0], 0: fish_dict[1], 1: fish_dict[2], 2: fish_dict[3], 3: fish_dict[4],
                             4: fish_dict[5], 5: fish_dict[6], 6: fish_dict[0] + fish_dict[7], 7: fish_dict[8]}
            fish_dict = new_fish_dict
        return sum(fish_dict.values())


if __name__ == '__main__':
    day6 = Day6('resources/input6')
    print(day6.part1())
    print(day6.part2())
