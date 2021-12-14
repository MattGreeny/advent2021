import unittest
from src.main.Day14 import Day14


class TestDay14(unittest.TestCase):

    def setUp(self):
        self.sut = Day14('resources/test14')

    def testSampleInputPart1(self):
        # When
        actual = self.sut.part1()

        # Then
        assert(actual == 1588)

    def testSampleInputPart2(self):
        # When
        actual = self.sut.part2()

        # Then
        assert(actual == 2188189693529)
