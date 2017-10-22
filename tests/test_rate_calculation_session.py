__author__ = 'RobertaBtt'

from rate_calculation import CsvParser
from rate_calculation import RateCalculationSession
import unittest


class TestRateCalculationSession(unittest.TestCase):

    def setUp(self):
        self.csv_file_path = 'data.csv'
        self.rate_calculation_session = RateCalculationSession.RateCalculationSession()

    def test_isnot_amount_available(self):
        offers = CsvParser.CsvParser.get_rows(self.csv_file_path)
        loan_amount = 10000
        self.assertEqual(False, self.rate_calculation_session.is_loan_possible( offers, loan_amount))

    def test_is_amount_available(self):
        offers = CsvParser.CsvParser.get_rows(self.csv_file_path)
        loan_amount = 1000
        self.assertEqual(True, self.rate_calculation_session.is_loan_possible( offers, loan_amount))
