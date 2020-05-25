import os.path
import sys
sys.path.append(os.path.abspath('.'))
from lib.transaction import Transaction


class TransactionHistory():
    def __init__(self):
        self._history = []

    def add(self, amount, category, old_balance):
        self._history.append(Transaction(
            amount, category, old_balance))
        return self._history[0]

    def get_history(self):
        return self._history
