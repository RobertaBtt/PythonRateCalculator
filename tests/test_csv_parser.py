__author__ = 'RobertaBtt'


import unittest

from rate_calculation import CsvParser

class TestCsvParrser(unittest.TestCase):

    def test_csv_parser_rows(self):

        csvfile = 'data.csv'

        rows = CsvParser.CsvParser.get_n_records_from_csv(csvfile)

        self.assertEqual(rows, 6)
