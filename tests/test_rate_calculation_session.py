__author__ = 'RobertaBtt'

from rate_calculation import CsvParser
from rate_calculation import RateCalculationSession
import unittest


class TestRateCalculationSession(unittest.TestCase):

    def setUp(self):
        self.csv_file_path = 'data.csv'
        self.rate_calculation_session = RateCalculationSession.RateCalculationSession()
        self.offers = CsvParser.CsvParser.get_rows(self.csv_file_path)

    def test_isnot_amount_available(self):
        loan_amount = 10000
        self.assertEqual(False, self.rate_calculation_session.is_loan_possible(self.offers, loan_amount))

    def test_is_amount_available(self):
        loan_amount = 1000
        self.assertEqual(True, self.rate_calculation_session.is_loan_possible(self.offers, loan_amount))

    def test_get_rates(self):
        loan_amount = 1000
        self.assertEqual(True, self.rate_calculation_session.get_rates(self.offers, loan_amount))

