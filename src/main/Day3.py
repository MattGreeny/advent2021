from main.InputReader import InputReader


class Day3:

    def __init__(self, file):
        self.data = InputReader.get_data_str(file)

    def part1(self):
        gamma = ""
        epsilon = ""
        for i in range(len(self.data[0])):
            total_ones = 0
            total_zeros = 0
            for number in self.data:
                if number[i] == "1":
                    total_ones += 1
                else:
                    total_zeros += 1
            if total_ones > total_zeros:
                gamma += "1"
                epsilon += "0"
            else:
                gamma += "0"
                epsilon += "1"
        return int(gamma, 2) * int(epsilon, 2)

    def part2(self):
        old_list_o2 = self.data.copy()
        new_list_o2 = self.data.copy()
        for i in range(len(self.data[0])):
            if len(new_list_o2) > 1:
                total_ones = 0
                total_zeros = 0
                for number in old_list_o2:
                    if number[i] == "1":
                        total_ones += 1
                    else:
                        total_zeros += 1
                if total_ones >= total_zeros:
                    new_list_o2 = [j for j in old_list_o2 if j[i] == "1"]
                else:
                    new_list_o2 = [j for j in old_list_o2 if j[i] == "0"]
                old_list_o2 = new_list_o2

        old_list_co2 = self.data.copy()
        new_list_co2 = self.data.copy()
        for i in range(len(self.data[0])):
            if len(new_list_co2) > 1:
                total_ones = 0
                total_zeros = 0
                for number in old_list_co2:
                    if number[i] == "1":
                        total_ones += 1
                    else:
                        total_zeros += 1
                if total_zeros <= total_ones:
                    new_list_co2 = [j for j in old_list_co2 if j[i] == "0"]
                else:
                    new_list_co2 = [j for j in old_list_co2 if j[i] == "1"]
                old_list_co2 = new_list_co2
        return int(new_list_o2[0], 2) * int(new_list_co2[0], 2)


if __name__ == '__main__':
    day3 = Day3('resources/input3')
    print(day3.part1())
    print(day3.part2())
