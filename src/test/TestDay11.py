import unittest
from src.main.Day11 import Day11


class TestDay11(unittest.TestCase):

    def setUp(self):
        self.sut = Day11('resources/test11')

    def testSampleInputPart1(self):
        # When
        actual = self.sut.part1()

        # Then
        assert(actual == 1656)

    def testSampleInputPart2(self):
        # When
        actual = self.sut.part2()

        # Then
        assert(actual == 195)
