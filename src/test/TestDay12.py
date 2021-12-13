import unittest
from src.main.Day12 import Day12


class TestDay12(unittest.TestCase):

    def setUp(self):
        self.sut = Day12('resources/test12')

    def testSampleInputPart1(self):
        # When
        actual = self.sut.part1()

        # Then
        assert(actual == 226)

    def testSampleInputPart2(self):
        # When
        actual = self.sut.part2()

        # Then
        assert(actual == 3509)
