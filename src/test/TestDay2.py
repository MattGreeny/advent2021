import unittest
from src.main.Day2 import Day2


class TestDay2(unittest.TestCase):

    def setUp(self):
        self.sut = Day2('resources/test2')

    def testSampleInputPart1(self):
        # When
        actual = self.sut.part1()

        # Then
        assert(actual == 150)

    def testSampleInputPart2(self):
        # When
        actual = self.sut.part2()

        # Then
        print(actual)
        assert(actual == 900)
