

class PrintStatement():
    def __init__(self, history):
        self.history = history

    def get_printout(self):
        for trans in self.history.get_history():
            print_str = f"{trans.category}: {trans.amount:.2f}, BALANCE: {trans.balance:.2f}"
            print(print_str)
