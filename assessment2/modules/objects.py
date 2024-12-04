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
        return self.store_locations.keys()

    def revenue_location(self, transactions, name):
        return sum([int(transactions[x][11]) for x in self.store_locations[name]])

    def revenue_each_location(self, transactions):
        dict = {}
        for i in self.store_locations().keys():
            dict[i] = self.revenue_location(transactions, i)
        return dict

    def ratings(self, transactions, store):
        return sum([float(transactions[x][-2]) for x in self.store_locations[store]]) / len(self.store_locations[store])

    def rating_each_location(self, transactions):
        dict = {}
        for i in self.store_locations().keys():
            dict[i] = self.ratings(transactions, i)
        return dict

    def best_selling_location(self, transactions, name):
        dict = {}
        for i in self.store_locations[name]:
            if i[2] in dict.keys():
                dict[i] += float(transactions[i][11])
            else:
                dict[i] = float(transactions[i][11])
        return max(dict, key=dict.get)

    def best_selling_each(self, transactions):
        dict = {}
        for i in self.store_locations().keys():
            dict[i] = self.best_selling_location(transactions, i)

        return dict

class categories:
    def __init__(self, dict):
        self.categories = dict
        self.number_of_categories = len(dict.keys())