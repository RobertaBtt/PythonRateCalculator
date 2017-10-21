__author__ = 'RobertaBtt'

from rate_calculation import CsvParser
from rate_calculation import RateCalculationSession
import unittest


class TestRateCalculationSession(unittest.TestCase):

    def test_get_rate(self):

        rateCalculationSession = RateCalculationSession.RateCalculationSession()
        csvfile = 'data.csv'
        rows = CsvParser.CsvParser.get_rows(csvfile)
        rateCalculationSession.get_rate_from_offers(rows)

        self.assertEqual(len(rateCalculationSession.get_offers()), 6)
