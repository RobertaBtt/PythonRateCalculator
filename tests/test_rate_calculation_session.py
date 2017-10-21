__author__ = 'RobertaBtt'

from rate_calculation import CsvParser
from rate_calculation import RateCalculationSession
import unittest


class TestRateCalculationSession(unittest.TestCase):

    def test_get_rate(self):

        rateCalculationSession = RateCalculationSession.RateCalculationSession()
        csvfile = 'data.csv'
        rows = CsvParser.CsvParser.get_rows(csvfile)
        lowest_rate = rateCalculationSession.get_lowest_rate(rows)

        self.assertEqual(lowest_rate, 0.069)

    def test_is_amount_available(self):

        rateCalculationSession = RateCalculationSession.RateCalculationSession()
        csvfile = 'data.csv'
        rows = CsvParser.CsvParser.get_rows(csvfile)
        availability = rateCalculationSession.get_availability(rows, 9090)
        self.assertEqual(False, availability)

        availability = rateCalculationSession.get_availability(rows, 2330)
        self.assertEqual(True, availability)

