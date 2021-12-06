import unittest
from src.main.Day5 import Day5


class TestDay5(unittest.TestCase):

    def setUp(self):
        self.sut = Day5('resources/test5')

    def testSampleInputPart1(self):
        # When
        actual = self.sut.part1()

        # Then
        assert(actual == 5)

    def testSampleInputPart2(self):
        # When
        actual = self.sut.part2()

        # Then
        assert(actual == 12)
