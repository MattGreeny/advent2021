import unittest
from src.main.Day4 import Day4


class TestDay4(unittest.TestCase):

    def setUp(self):
        self.sut = Day4('resources/test4')

    def testSampleInputPart1(self):
        # When
        actual = self.sut.part1()

        # Then
        assert(actual == 4512)

    def testSampleInputPart2(self):
        # When
        actual = self.sut.part2()

        # Then
        assert(actual == 1924)
