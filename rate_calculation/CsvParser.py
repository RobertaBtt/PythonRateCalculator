__author__ = 'RobertaBtt'

import csv

from collections import OrderedDict

class CsvParser():
    class __CsvParser:
        def __init__(self):
            self.game_sessions = {}
        def __str__(self):
            return repr(self)
    instance = None
    def __init__(self):
        if not CsvParser.instance:
            CsvParser.instance = CsvParser.__CsvParser()

    def __getattr__(self, name):
        return  getattr(self.instance, name)
    

    @staticmethod
    def get_rows(csvfilePath):
        rows = []


        try:

            with open(csvfilePath, "r") as csvfile:
                file = csv.reader(csvfile)
                next(file)

                for Lender,Rate,Available in file:
                    rows.append((Rate,Available))


            return sorted(rows)


        except Exception:
            print Exception

