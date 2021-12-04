from main.InputReader import InputReader


class Day4:

    def __init__(self, file):
        self.data = InputReader.get_data_str(file)
        self.grids = []

    def part1(self):
        numbers = [int(x) for x in self.data[0].split(',')]
        grids = []
        for i in range(2, len(self.data), 6):
            grids.append(BingoGrid([self.data[i + j] for j in range(5)]))
        for number in numbers:
            for grid in grids:
                grid.mark_number(number)
                if grid.has_bingo():
                    return grid.calculate_score(number)
        print('FAILED')

    def part2(self):
        grids = []
        for i in range(2, len(self.data), 6):
            grids.append(BingoGrid([self.data[i + j] for j in range(5)]))
        numbers = [int(x) for x in self.data[0].split(',')]
        for number in numbers:
            new_grids = []
            for grid in grids:
                grid.mark_number(number)
                if grid.has_bingo():
                    if len(grids) == 1:
                        return grid.calculate_score(number)
                else:
                    new_grids.append(grid)
            grids = new_grids


class BingoGrid:

    def __init__(self, columns):
        self.columns = []
        for column in columns:
            self.columns.append([int(x) for x in list(filter(lambda y: y != '', column.split(' ')))])
        self.rows = [[column[i] for column in self.columns] for i in range(5)]

    def mark_number(self, number):
        for column in self.columns:
            if number in column:
                column.remove(number)
        for row in self.rows:
            if number in row:
                row.remove(number)

    def has_bingo(self):
        for column in self.columns:
            if len(column) == 0:
                return True
        for row in self.rows:
            if len(row) == 0:
                return True
        return False

    def calculate_score(self, number):
        total_sum = 0
        for row in self.rows:
            total_sum += sum(row)
        return total_sum * number


if __name__ == '__main__':
    day4 = Day4('resources/input4')
    print(day4.part1())
    print(day4.part2())
