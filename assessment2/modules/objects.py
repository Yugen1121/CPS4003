import modules.helpers
from modules.helpers import find_best


class Payment:
    def __init__(self, method):
        # takes the input method and assigns it to method
        self.method = method
        self.revenue = 0
        self.count = 0

class Payment_methods:
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


class Store:
    def __init__(self, location):
        self.store_name = location
        self.transactionsID = []
        self.revenue = 0
        self.rating = 0
        self.categories = {}
        self.payment_methods = {}

    # Returns the details about the store
    def details(self):
        return {"Loaction": self.store_name, "Revenue" : self.revenue, "Total unit Sold": self.categories.total_unit(), "Rating": self.rating}

    # Returns the most popular category
    def popular_category(self):
        return self.categories.popular()

    # Returns the category with the most revenue
    def most_revenue_category(self):
        return self.categories.most_revenue()

    # Returns all teh category soled in the store
    def all_categories(self):
        return self.categories.return_categories()


class Store_locations:
    def __init__(self):
        # takes store location as key and stores the store object as values
        self.store_locations = {}

    def details(self):
        x = []
        for i in self.store_locations.values():
            x.append(i.details())

        return x

class Category:
    def __init__(self, name):
        self.name = name
        self.count = 0
        self.revenue = 0
        self.unit_sold = 0

class Categories:
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

    # Returns all the total unit sold
    def total_unit(self):
        sum = 0
        for i in self.categories:
            sum += i.unit_sold
        return sum


class Transactions:
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
