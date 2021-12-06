import unittest
from src.main.Day6 import Day6


class TestDay6(unittest.TestCase):

    def setUp(self):
        self.sut = Day6('resources/test6')

    def testSampleInputPart1(self):
        # When
        actual = self.sut.part1()

        # Then
        assert(actual == 5934)

    def testSampleInputPart2(self):
        # When
        actual = self.sut.part2()

        # Then
        assert(actual == 26984457539)
