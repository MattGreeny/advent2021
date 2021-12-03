import unittest
from src.main.Day3 import Day3


class TestDay3(unittest.TestCase):

    def setUp(self):
        self.sut = Day3('resources/test3')

    def testSampleInputPart1(self):
        # When
        actual = self.sut.part1()

        # Then
        assert(actual == 198)

    def testSampleInputPart2(self):
        # When
        actual = self.sut.part2()

        # Then
        assert(actual == 230)
