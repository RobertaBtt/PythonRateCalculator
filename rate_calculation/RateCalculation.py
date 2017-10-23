#-*- coding: utf-8 -*-
__author__ = 'RobertaBtt'

import sys
import CsvParser
import math

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
        if loan_amount>0:
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

    def get_repayment_avg_tax(self, rates_list):
        """
        :param rates_list: a tuple containing all the taxes
        :return: the avg of the taxes
        """
        if len(rates_list) > 0:
            avg_rates = sum([v[0] for v in rates_list]) / float(len(rates_list))
            return round(avg_rates, 2)

        return 0

    def get_repayment(self, num_units_per_year, loan_amount, tax_rate, total_of_units):
        """
        :param num_units_per_year: how many payment in a year
        :param loan_amount:  what is the amout of the requested load
        :param tax_rate: the tax rate applied
        :param total_of_units: total of number of payments
        :return: the payment for unit
        """

        if (num_units_per_year > 0 and loan_amount > 0 and tax_rate > 0 and total_of_units > 0):

            tax_rate_per_units = tax_rate/num_units_per_year
            payment = ( tax_rate_per_units * loan_amount) / (1-(1+tax_rate_per_units)**(-total_of_units))
            return payment

        return 0
