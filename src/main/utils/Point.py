class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def all_neighbours(self):
        return self.neighbours() + [self.north_east(), self.south_east(), self.south_west(), self.north_west()]

    def neighbours(self):
        return [self.north(), self.south(), self.east(), self.west()]

    def north(self):
        return Point(self.x, self.y + 1)

    def south(self):
        return Point(self.x, self.y - 1)

    def east(self):
        return Point(self.x + 1, self.y)

    def west(self):
        return Point(self.x - 1, self.y)

    def north_east(self):
        return Point(self.x + 1, self.y + 1)

    def south_east(self):
        return Point(self.x - 1, self.y + 1)

    def south_west(self):
        return Point(self.x - 1, self.y - 1)

    def north_west(self):
        return Point(self.x + 1, self.y - 1)

