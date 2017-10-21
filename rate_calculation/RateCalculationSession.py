#-*- coding: utf-8 -*-
__author__ = 'RobertaBtt'

import sys
import CsvParser


class RateCalculationSession():
    class __RateCalculationSession:
        def __init__(self):
            self.offers = []
        def __str__(self):
            return repr(self)
    instance = None
    def __init__(self):
        if not RateCalculationSession.instance:
            RateCalculationSession.instance = RateCalculationSession.__RateCalculationSession()

    def __getattr__(self, name):
        return  getattr(self.instance, name)

    def __init__(self):
        self.offers = []

    def get_lowest_rate(self, offers):
        lowest_rate = offers[0]
        return float(lowest_rate[0]) - 0.01





#====================================
if __name__ == '__main__':

    csvfile = sys.argv[1]
    requestedAmount = sys.argv[2]
    rateCalculationSession = RateCalculationSession()

    offers = CsvParser.CsvParser.get_rows(csvfile)
    lowest_rate = rateCalculationSession.get_lowest_rate(offers)

    print "Requested amount: £", requestedAmount
    print "Rate:", lowest_rate