__author__ = 'RobertaBtt'

import csv


class CsvParser:

    class __CsvParser:

        def __str__(self):
            return repr(self)
    instance = None

    def __init__(self):
        if not CsvParser.instance:
            CsvParser.instance = CsvParser.__CsvParser()

    def __getattr__(self, name):
        return getattr(self.instance, name)

    @staticmethod
    def get_rows(csv_file_path):
        """

        :param csvfilePath: the path of the csv file
        :return: rows Lender and Rate
        """
        try:
            return CsvParser.__get_rows(csv_file_path)

        except Exception as e:
            raise e

    @staticmethod
    def get_rows_sorted_by_rate(csv_file_path):
        """
        :param csvfilePath: the path of the csv file
        :return: rows Rate and Available sorted by Rate
        """
        try:
            return sorted(CsvParser.__get_rows(csv_file_path),  key=lambda row: float(row[0]))

        except Exception as e:
            raise e

    @staticmethod
    def get_rows_sorted_by_available(csv_file_path):
        """
        :param csvfilePath: the path of the csv file
        :return: rows Rate and Available sorted by Available
        """
        try:
            return sorted(CsvParser.__get_rows(csv_file_path), key=lambda row: int(row[1]))

        except Exception as e:
            raise e

    @classmethod
    def __get_rows(self, csv_file_path):

        rows = []

        try:
            with open(csv_file_path, "r") as csvfile:
                file = csv.reader(csvfile)
                next(file)

                for Lender,Rate,Available in file:
                    rows.append((Rate,Available))
            return rows
        except Exception as e:
            raise e

