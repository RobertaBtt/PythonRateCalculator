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

    def get_rates(self, csv_file_path, loan_amount, total_of_units):
        """

        :param csv_file_path: the path of the data file
        :param loan_amount: request amount
        :return: dictionary: repayment per unit, and the tax applied
        """

        offers = self.csv_parser.get_rows_sorted_by_rate(csv_file_path)

        if self.is_loan_possible(offers, loan_amount):
            rates = self.rate_calculation.get_rates(offers, loan_amount)
            avg_rate = self.rate_calculation.get_repayment_avg_tax(rates)
            num_units_per_year = 12
            repayment_per_unit = self.rate_calculation.get_repayment(num_units_per_year, loan_amount, avg_rate, total_of_units)

            return {'repayment' : repayment_per_unit, 'rate': avg_rate}
        else:
            return {'not_available': "Amount not available"}

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

    try:
        csv_file_path = sys.argv[1]
        loan_amount = float(sys.argv[2])
        # csv_file_path = 'data.csv'
        # loan_amount = 10000

        total_of_units = 36
        rateCalculationSession = RateCalculationSession()

        rates = rateCalculationSession.get_rates(csv_file_path, loan_amount, total_of_units)

        print "Requested amount: £", loan_amount
        if rates.has_key('not_available'):
            print rates['not_available']
        else:
            if rates.has_key('rate'): print "Rate:", round(rates['rate']*100, 1), "%"
            if rates.has_key('repayment'):
                print "Monthly repayment: £", round(rates['repayment'], 2), "%"
                print "Total repayment: £", round(rates['repayment']*total_of_units, 2)
    except Exception as e:
        print "Please check parameters/data"
        print "Message:", e.message




