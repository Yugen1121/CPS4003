class payment:
    def __init__(self, method):
        # takes the input method and assigns it to method
        self.method = method
        self.revenue = 0

class payment_methods:
    def __init__(self):
        # takes method name as key and payment class as values
        self.methods = {}

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
        self.category = []

class categories:
    def __init__(self):
        # takes category name as key and stores category object as values
        self.categories = {}


class transactions:
    def __init__(self):
        # takes transaction id as key and record as value
        self.transactions = {}
        self.revenue = 0
        self.rating = 0
        self.stores = store_locations()
        self.categories = categories()
        self.payments = payment_methods()

    def transaction(self, transactionID):
        return self.transactions[transactionID]

    def show_stores(self):
        return self.store_locations.keys()

    def show_categories(self):
        return self.categories.categories.keys()

    def revenue(self):
        return self.revenue

    def rating(self):
        return self.rating

    def payment_method(self):
        return self.payments.payment_methods.keys()
