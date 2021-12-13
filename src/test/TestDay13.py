import unittest
from src.main.Day13 import Day13


class TestDay13(unittest.TestCase):

    def setUp(self):
        self.sut = Day13('resources/test13')

    def testSampleInputPart1(self):
        # When
        actual = self.sut.part1()

        # Then
        assert(actual == 17)

    def testSampleInputPart2(self):
        # When
        actual = self.sut.part2()
