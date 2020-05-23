class Transaction():
    def __init__(self, amount, category):
        self._amount = amount
        self._category = category

    @property
    def amount(self):
        return self._amount

    @property
    def category(self):
        return self._category
