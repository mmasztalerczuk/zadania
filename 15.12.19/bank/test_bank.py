import unittest
from .bank import Account, Card


class AccountTest(unittest.TestCase):
    def test01_simple_test(self):
        # given
        number = 123123
        name = "John"
        surname = "Doe"

        # when
        account = Account(id_account=number, name=name, surname=surname)

        # then
        self.assertEqual((name, surname), account.owner())
        self.assertEqual(number, account.number())
        self.assertEqual(str(number), str(account))

    def test02_simple_transer(self):
        # given
        number = 123123
        name = "John"
        surname = "Doe"
        money = 312
        account = Account(id_account=number, name=name, surname=surname)

        # when
        account.transfer(money)

        # then
        self.assertEqual(money, account.balance())

    def test03_bigger_transer(self):
        # given
        number = 123123
        name = "John"
        surname = "Doe"
        money = 312
        money2 = -100
        account = Account(id_account=number, name=name, surname=surname)

        # when
        account.transfer(money)
        account.transfer(money2)

        # then
        self.assertEqual(money + money2, account.balance())


class CardTest(unittest.TestCase):
    def setUp(self):
        number = 123123
        name = "John"
        surname = "Doe"
        self.account = Account(id_account=number, name=name, surname=surname)

    def test01_simple_test(self):
        # given
        pin = 1234
        card = Card(pin, self.account)

        self.assertEqual(True, card.check_pin(pin))
        self.assertEqual(False, card.check_pin(3122))

    def test02_owner(self):
        # given
        pin = 1234
        card = Card(pin, self.account)

        self.assertEqual(self.account, card.get_account())
