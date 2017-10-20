__author__ = 'RobertaBtt'

import csv
class CsvParser():

    @staticmethod
    def get_n_records_from_csv(csvfilePath):

        try:
            with open(csvfilePath, 'rb') as csvfile:
                rows = csv.reader(csvfile)
                return sum(1 for row in rows)

        except Exception:
            print Exception

