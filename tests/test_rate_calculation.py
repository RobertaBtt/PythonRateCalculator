__author__ = 'RobertaBtt'

from rate_calculation import CsvParser
from rate_calculation import RateCalculation
import unittest


class TestRateCalculation(unittest.TestCase):

    def setUp(self):
        self.csv_file_path = 'data.csv'
        self.rate_calculation = RateCalculation.RateCalculation()
        self.offers = CsvParser.CsvParser.get_rows_sorted_by_rate(self.csv_file_path)

    def test_get_rates_uncheked_amount(self):
        loan_amount = 10000
        self.assertEqual(7, len(self.rate_calculation.get_rates(self.offers, loan_amount)))

    def test_get_rates_checked_amount_1(self):
        loan_amount = 1000
        self.assertEqual(2, len(self.rate_calculation.get_rates(self.offers, loan_amount)))

    def test_get_rates_checked_amount_2(self):
        loan_amount = 1001
        self.assertEqual(3, len(self.rate_calculation.get_rates(self.offers, loan_amount)))

    def test_get_rates_checked_amount_2(self):
        loan_amount = 1001
        result = self.rate_calculation.get_rates(self.offers, loan_amount)
        self.assertEqual(480, result[0][1])
        self.assertEqual(520, result[1][1])
        self.assertEqual(1, result[2][1])

    def test_get_rates_checked_amount_3(self):
        loan_amount = 900
        result = self.rate_calculation.get_rates(self.offers, loan_amount)
        self.assertEqual(480, result[0][1])
        self.assertEqual(420, result[1][1])

