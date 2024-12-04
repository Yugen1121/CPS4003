class transactions:
    def __init__(self, dict):
        self.transactions = dict
        self.number_of_transaction = len(list)

    #returns record of transaction with the transactionID
    def tranaction(self, transactionID):
        return self.transactions[transactionID]

    def total_revenue(self):
        return sum([int(x[11]) for x in self.transactions.values()])

class store_locations:
    def __init__(self, dict):
        self.store_locations = dict
        self.number_of_locations = len(dict.keys())

    def list_store(self):
        return

class categories:
    def __init__(self, dict):
        self.categories = dict
        self.number_of_categories = len(dict.keys())