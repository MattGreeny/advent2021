from main.utils.Point import Point


class Grid:

    def __init__(self, map=None, width=None, height=None):
        self.map = map
        self.width = width
        self.height = height

    # def __str__(self):
    #     pass

    def is_in_range(self, point):
        return 0 <= point.x < self.height and 0 <= point.y < self.width

    def get_value(self, point):
        return self.map[point]

    def set_value(self, point, value):
        self.map[point] = value

    def increment_value(self, point):
        if type(self.map[point]) != int:
            raise Exception("Can only increment ints")
        self.set_value(point, self.get_value(point) + 1)

    def neighbours(self, point):
        return [neighbour for neighbour in point.neighbours() if self.is_in_range(neighbour)]

    def all_neighbours(self, point):
        return [neighbour for neighbour in point.all_neighbours() if self.is_in_range(neighbour)]

    def transpose(self):
        new_map = {}
        for point, value in self.map.items():
            new_map[Point(point.y, point.x)] = value
        self.map = new_map
