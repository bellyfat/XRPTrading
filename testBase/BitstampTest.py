import unittest

from constconfig import CUSTOMER_ID
from exchangeConnection.Bitstamp import Bitstamp


class BitstampConnectionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cfg = '../environment.yml'
        cls.bitstamp_connection = Bitstamp(cls.cfg)

    def test_get_customer_id(self):
        assert (self.bitstamp_connection.get_customer_id() == CUSTOMER_ID)

    def test_get_currency_pair_balance(self):
        # currency_pair = 'xrpusd'
        self.bitstamp_connection.get_currency_pair_balance()
