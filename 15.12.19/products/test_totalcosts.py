import unittest
from .totalcosts import TotalCosts


class TotalCostTest(unittest.TestCase):
    def test01_simple_test(self):
        # given
        products = [{"name": "Milk", "price": 1, "quantity": 1}]
        total = TotalCosts()

        # then
        self.assertEqual(1, total.get_total_price(products))

    def test02_more_products(self):
        # given
        products = [
            {"name": "Milk", "price": 1, "quantity": 1},
            {"name": "Carrot", "price": 12, "quantity": 1},
            {"name": "Chips", "price": 13, "quantity": 2},
        ]
        total = TotalCosts()

        # then
        self.assertEqual(39, total.get_total_price(products))

    def test03_simple_discount(self):
        # given
        products = [
            {"name": "Milk", "price": 1, "quantity": 1},
            {"name": "Carrot", "price": 12, "quantity": 1},
            {"name": "Chips", "price": 13, "quantity": 2},
        ]
        total = TotalCosts(["Milk"])

        # then
        self.assertEqual(38.8, total.get_total_price(products))

    def test03_bigger_discount(self):
        # given
        products = [
            {"name": "Milk", "price": 1, "quantity": 1},
            {"name": "Carrot", "price": 12, "quantity": 1},
            {"name": "Chips", "price": 13, "quantity": 2},
        ]
        total = TotalCosts(["Milk", "Carrot"])

        # then
        self.assertEqual(36.4, total.get_total_price(products))
