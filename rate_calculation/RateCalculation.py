#-*- coding: utf-8 -*-
__author__ = 'RobertaBtt'

import sys
import CsvParser

class RateCalculation():
    class __RateCalculation:

        def __init__(self):
            self.offers = []

        def __str__(self):
            return repr(self)
    instance = None

    def __init__(self):
        if not RateCalculation.instance:
            RateCalculation.instance = RateCalculation.__RateCalculation()

    def __getattr__(self, name):
        return  getattr(self.instance, name)

    def __init__(self):
        self.offers = []

    def get_rates(self, offers, loan_amount):
        return 0
