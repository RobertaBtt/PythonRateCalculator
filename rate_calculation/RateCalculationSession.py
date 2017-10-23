#-*- coding: utf-8 -*-
__author__ = 'RobertaBtt'

import sys
import CsvParser
import RateCalculation

class RateCalculationSession():

    class __RateCalculationSession:
        def __init__(self):
            self.rate_calculation = RateCalculation.RateCalculation()
            self.csv_parser = CsvParser.CsvParser()

        def __str__(self):
            return repr(self)
    instance = None
    def __init__(self):
        if not RateCalculationSession.instance:
            RateCalculationSession.instance = RateCalculationSession.__RateCalculationSession()

    def __getattr__(self, name):
        return  getattr(self.instance, name)

    def __init__(self):
        self.rate_calculation = RateCalculation.RateCalculation()
        self.csv_parser = CsvParser.CsvParser()

    def get_rates(self, csv_file_path, loan_amount):
        """

        :param csv_file_path: the path of the data file
        :param loan_amount: request amount
        :return:
        """

        offers = self.csv_parser.get_rows_sorted_by_rate(csv_file_path)

        if self.is_loan_possible(offers, loan_amount):
            result = self.rate_calculation.get_rates(offers, loan_amount)
            return result
        else:
            return "Amount not available"

    def is_loan_possible(self, offers, loan_amount):
        """
        :param offers: list of offers from the pool of lenders
        :param loan_amount: request amount
        :return:
        """

        total_available = sum([float(pair[1]) for pair in offers])
        return loan_amount <= total_available





#====================================
if __name__ == '__main__':

    # csv_file_path = sys.argv[1]
    # loan_amount = sys.argv[2]

    # print "Requested amount: £", loan_amount

    rateCalculationSession = RateCalculationSession()
    # print rateCalculationSession.get_rates(csv_file_path, loan_amount)

    result = rateCalculationSession.get_rates('data.csv', 1023)
    print result