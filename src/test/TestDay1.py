import unittest
from src.main.Day1 import Day1


class TestDay1(unittest.TestCase):

    def setUp(self):
        self.sut = Day1('resources/test1')

    def testSampleInputPart1(self):
        # When
        actual = self.sut.part1()

        # Then
        assert(actual == 5)

    def testSampleInputPart2(self):
        # When
        actual = self.sut.part2()

        # Then
        assert(actual == 5)
