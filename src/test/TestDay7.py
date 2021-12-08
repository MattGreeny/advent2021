import unittest
from src.main.Day7 import Day7


class TestDay7(unittest.TestCase):

    def setUp(self):
        self.sut = Day7('resources/test7')

    def testSampleInputPart1(self):
        # When
        actual = self.sut.part1()

        # Then
        assert(actual == 37)

    def testSampleInputPart2(self):
        # When
        actual = self.sut.part2()

        # Then
        assert(actual == 168)
