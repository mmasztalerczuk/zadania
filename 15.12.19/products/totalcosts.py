class TotalCosts:
    def __init__(self, discounts=None):
        self._discounts = discounts if discounts else []

    def get_total_price(self, products):
        total_price = 0
        for product in products:
            if product["name"] in self._discounts:
                price = 0.8
            else:
                price = 1
            total_price += product["quantity"] * product["price"] * price

        return total_price
