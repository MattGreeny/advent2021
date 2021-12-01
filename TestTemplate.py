import unittest
from src.main.DayX import DayX


class TestDayX(unittest.TestCase):

    def setUp(self):
        self.sut = DayX('resources/testX')

    def testSampleInputPart1(self):
        # Given
        # sut = DayX('resources/testX')

        # When
        actual = self.sut.part1()

        # Then
        assert(actual == 123)

    def testSampleInputPart2(self):
        # Given
        # sut = DayX('resources/testX')

        # When
        actual = self.sut.part2()

        # Then
        assert(actual == 123)
