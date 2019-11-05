from unittest import TestCase
from ngpayetax.index import PayeTax

class TestPayeTax(TestCase):
    def setUp(self):
        self.annual_taxable_income = 1225500
        self.paye =  PayeTax(self.annual_taxable_income)

    def test_annual(self):
        self.assertEqual(152845, round(self.paye.annual(), 0))

    def test_monthly(self):
        self.assertEqual(12737.08, round(self.paye.annual()/12, 2))
