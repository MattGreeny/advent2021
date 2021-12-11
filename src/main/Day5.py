from main.utils.InputReader import InputReader


class Day5:

    def __init__(self, file):
        self.data = InputReader.get_data_str(file)
        self.size = 1000

    def part1(self):
        board = [[0] * self.size for _ in range(self.size)]
        for line in self.data:
            start, finish = line.split(' -> ')
            start_x, start_y = start.split(',')
            finish_x, finish_y = finish.split(',')

            start_x = int(start_x)
            start_y = int(start_y)
            finish_x = int(finish_x)
            finish_y = int(finish_y)

            if start_x == finish_x:
                for i in range(min(start_y, finish_y), max(start_y, finish_y) + 1):
                    board[start_x][i] += 1
            elif start_y == finish_y:
                for i in range(min(start_x, finish_x), max(start_x, finish_x) + 1):
                    board[i][start_y] += 1
        count = 0
        for i in range(self.size):
            for j in range(self.size):
                if board[i][j] > 1:
                    count += 1
        return count

    def part2(self):
        board = [[0] * self.size for _ in range(self.size)]
        for line in self.data:
            start, finish = line.split(' -> ')
            start_x, start_y = start.split(',')
            finish_x, finish_y = finish.split(',')

            start_x = int(start_x)
            start_y = int(start_y)
            finish_x = int(finish_x)
            finish_y = int(finish_y)

            if start_x == finish_x:
                for i in range(min(start_y, finish_y), max(start_y, finish_y) + 1):
                    board[start_x][i] += 1
            elif start_y == finish_y:
                for i in range(min(start_x, finish_x), max(start_x, finish_x) + 1):
                    board[i][start_y] += 1
            else:
                if start_x < finish_x and start_y < finish_y:  # 1,1 -> 3,3
                    for i in range(finish_x - start_x + 1):
                        board[start_x + i][start_y + i] += 1
                elif start_x > finish_x and start_y > finish_y:   # 3,3 -> 1,1
                    for i in range(start_x - finish_x + 1):
                        board[start_x - i][start_y - i] += 1
                elif start_x > finish_x and start_y < finish_y:   # 3,1 -> 1,3
                    for i in range(start_x - finish_x + 1):
                        board[start_x - i][start_y + i] += 1
                elif start_x < finish_x and start_y > finish_y:   # 1,3 -> 3,1
                    for i in range(finish_x - start_x + 1):
                        board[start_x + i][start_y - i] += 1
        count = 0
        for i in range(self.size):
            for j in range(self.size):
                if board[i][j] > 1:
                    count += 1
        return count


if __name__ == '__main__':
    day5 = Day5('resources/input5')
    print(day5.part1())
    print(day5.part2())
