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
        return getattr(self.instance, name)

    def __init__(self):
        self.offers = []

    def get_rates(self, offers, loan_amount):
        amount_reached = 0.0

        rates = []
        for index, offer in enumerate(offers):

            amount_reached += float(offer[1])
            if amount_reached < loan_amount:
                rates.append((float(offer[0]), float(offer[1])))

            elif amount_reached == loan_amount:
                rates.append((float(offer[0]), float(offer[1])))
                return rates
            elif amount_reached > loan_amount:
                rates.append((float(offer[0]), float(offer[1]) - (amount_reached - loan_amount)))
                return rates

        return rates
