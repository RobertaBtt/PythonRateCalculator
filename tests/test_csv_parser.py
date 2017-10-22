__author__ = 'RobertaBtt'

from rate_calculation import CsvParser
import unittest


class TestCsvParser(unittest.TestCase):

    def setUp(self):
        self.csv_file_path = 'data.csv'

    def test_csv_parser_rows(self):
        rows = CsvParser.CsvParser.get_rows(self.csv_file_path)
        self.assertEqual(len(rows), 7)

    def test_csv_parser_rows_sorted_available(self):
        rows = CsvParser.CsvParser.get_rows_sorted_by_rate(self.csv_file_path)
        self.assertEqual(rows[0][0], 0.069)

    def test_csv_parser_rows_sorted_available(self):
        rows = CsvParser.CsvParser.get_rows_sorted_by_available(self.csv_file_path)
        self.assertEqual(int(rows[0][1]), 60)
