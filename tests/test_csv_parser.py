__author__ = 'RobertaBtt'

from rate_calculation import CsvParser
import unittest


class TestCsvParser(unittest.TestCase):

    def test_csv_parser_rows(self):
        csvfile = 'data.csv'
        rows = CsvParser.CsvParser.get_rows(csvfile)
        self.assertEqual(len(rows), 7)
