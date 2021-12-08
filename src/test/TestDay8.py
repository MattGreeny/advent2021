import unittest
from src.main.Day8 import Day8


class TestDay8(unittest.TestCase):

    def setUp(self):
        self.sut = Day8('resources/test8')

    def testSampleInputPart1(self):
        # When
        actual = self.sut.part1()

        # Then
        assert(actual == 26)

    def testSampleInputPart2(self):
        # When
        actual = self.sut.part2()

        # Then
        assert(actual == 61229)
