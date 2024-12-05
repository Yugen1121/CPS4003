import modules.helpers

from assessment2.modules.helpers import find_best


class payment:
    def __init__(self, method):
        # takes the input method and assigns it to method
        self.method = method
        self.revenue = 0
        self.count = 0

class payment_methods:
    def __init__(self):
        # takes method name as key and payment class as values
        self.methods = {}

    # returns all the payment methods used
    def payment_method(self):
        return methods.keys()

    # returns the payment method with the most revenue
    def most_revenue(self):
        max = ["", 0]
        for i in self.methods:
            max = find_best([i.name, i.revenue], max)
        return max

    # returns the most used payment method
    def most_used(self):
        max = ["", 0]
        for i in self.methods:
            max = find_best([i.name, i.count], max)
        return max

class store:
    def __init__(self, location):
        self.store_name = location
        self.transactionsID = []
        self.revenue = 0
        self.rating = 0
        self.categories = []
        self.payment_methods = []

class store_locations:
    def __init__(self):
        # takes store location as key and stores the store object as values
        self.store_locations = {}

class category:
    def __init__(self, name):
        self.name = name
        self.count = 0
        self.revenue = 0
        self.unit_sold = 0

class categories:
    def __init__(self):
        # takes category name as key and stores category object as values
        self.categories = {}

    # Returns all the category name
    def return_categories(self):
        return self.categories.keys()

    # returns the category with the most revenue
    def most_revenue(self):
        max = ["", 0]
        for i in self.categories:
            max = find_best([i.name, i.revenue], max)
        return max

    # returns the category with the most transaction
    def popular(self):
        max = ["", 0]
        for i in self.categories:
            max = find_best([i.name, i.count], max)
        return max

    # returns the category with the most unit sold
    def most_unit(self):
        max = ["", 0]
        for i in self.categories:
            max = find_best([i.name, i.unit_sold], max)
        return max


class transactions:
    def __init__(self):
        # takes transaction id as key and record as value
        self.transactions = {}
        self.revenue = 0
        self.rating = 0
        self.stores = store_locations()
        self.categories = categories()
        self.payments = payment_methods()

    # Takes transactionID as an input and returns record with the transactionID
    def transaction(self, transactionID):
        return self.transactions[transactionID]

    # returns all the store location
    def show_stores(self):
        return self.store_locations.keys()

    # returns all the category
    def show_categories(self):
        return self.categories.categories.return_categories()

    # returns all the payment methods used to pay
    def payment_method(self):
        return self.payments.payment_methods.keys()
