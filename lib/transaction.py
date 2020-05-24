class Transaction():
    def __init__(self, amount, category, old_balance):
        self._amount = amount
        self._category = category
        self._balance = self.__update_balance(amount, old_balance)

    @property
    def amount(self):
        return self._amount

    @property
    def category(self):
        return self._category

    @property
    def balance(self):
        return self._balance

    # private methods
    def __update_balance(self, amount, old_balance):
        self._balance = amount + old_balance
        return self._balance
