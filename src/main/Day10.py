from main.InputReader import InputReader


class Day10:

    def __init__(self, file):
        self.data = InputReader.get_data_str_list(file)

    def part1(self):
        counter = 0
        for line in self.data:
            counter += self.check_legal(line)
        return counter

    def check_legal(self, line):
        points = {')': 3, ']': 57, '}': 1197, '>': 25137}
        opposites = {')': '(', ']': '[', '}': '{', '>': '<'}
        stack = []
        for character in line:
            if character in '({[<':
                stack.append(character)
            else:
                if opposites[character] == stack[len(stack) - 1]:
                    stack.pop()
                else:
                    return points[character]
        return 0

    def part2(self):
        scores = []
        for line in self.data:
            scores.append(self.complete_stack(line))
        scores = [x for x in scores if x != 0]
        scores.sort()
        return scores[int((len(scores) - 1) / 2)]

    def complete_stack(self, line):
        points = {')': 1, ']': 2, '}': 3, '>': 4}
        opposites = {')': '(', ']': '[', '}': '{', '>': '<'}
        opposites_reversed = {v: k for k, v in opposites.items()}
        stack = []
        for character in line:
            if character in '({[<':
                stack.append(character)
            else:
                if opposites[character] == stack[len(stack) - 1]:
                    stack.pop()
                else:
                    return 0
        score = 0
        while len(stack) > 0:
            score *= 5
            score += points[opposites_reversed[stack.pop()]]
        return score


if __name__ == '__main__':
    day10 = Day10('resources/input10')
    print(day10.part1())
    print(day10.part2())
