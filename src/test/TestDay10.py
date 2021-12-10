import unittest
from src.main.Day10 import Day10


class TestDay10(unittest.TestCase):

    def setUp(self):
        self.sut = Day10('resources/test10')

    def testSampleInputPart1(self):
        # When
        actual = self.sut.part1()

        # Then
        assert(actual == 26397)

    def testSampleInputPart2(self):
        # When
        actual = self.sut.part2()

        # Then
        assert(actual == 288957)
