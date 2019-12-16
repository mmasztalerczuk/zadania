class Account:
    def __init__(self, id_account, name, surname):
        self._id_account = id_account
        self._name = name
        self._surname = surname
        self._balance = 0

    def __repr__(self):
        return str(self._id_account)

    def owner(self):
        return (self._name, self._surname)

    def balance(self):
        return self._balance

    def number(self):
        return self._id_account

    def transfer(self, value):
        self._balance += value


class Card:
    def __init__(self, pin, owner_account):
        self._owner_account = owner_account
        self._pin = pin

    def __repr__(self):
        return self._owner_account.owner[0] + " " + self._owner_account.owner[1]

    def check_pin(self, pin):
        if self._pin == pin:
            return True
        return False

    def get_account(self):
        return self._owner_account
