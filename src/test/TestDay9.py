import unittest
from src.main.Day9 import Day9


class TestDay9(unittest.TestCase):

    def setUp(self):
        self.sut = Day9('resources/test9')

    def testSampleInputPart1(self):
        # When
        actual = self.sut.part1()

        # Then
        assert(actual == 15)

    def testSampleInputPart2(self):
        # When
        actual = self.sut.part2()

        # Then
        assert(actual == 1134)
