import modules.helpers
import matplotlib.pyplot as plt
import tkinter as tk
from modules.helpers import find_best
import modules.ui as ui



class Plot:

    # Function to create a pie char
    def print_pie(self, labels, values, title):
        plt.pie(values, labels=labels, autopct='%1.1f%%')
        plt.title(title)
        plt.show()

    # Function to create a histogram
    def print_hist(self, list, title, xlabel, ylabel):
        fig, ax = plt.subplots(1, 1)
        ax.hist(list[1])

        # Set title
        ax.set_title(title)

        # adding labels
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)

        # Make some labels.
        rects = ax.patches

        for rect, label in zip(rects, list[0]):
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2, height + 0.01, label,
                    ha='center', va='bottom')

            # Show plot
        plt.show()



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
        self.categories = Categories()
        self.payment_methods = Payment_methods()
        self.transactions_bd = Transactions_bd()

    def __str__(self):

        payments = ""
        for i in self.payment_methods.methods.values():
            payments = payments + f"\t-{i.method}: {i.revenue}\n"
        return f"""    SALES REPORT
• Loaction: {self.store_name}
• Total transactions: {len(self.transactionsID)} 
• Total revenue: {self.revenue:.2f}
• Average transaction value: {(self.revenue/len(self.transactionsID)):.2f}
• Total quantity of products sold: {sum([i.unit_sold for i in self.categories.categories.values()]):.2f}
• Average customer satisfaction score: {self.rating:.2f}\n""" + payments

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

    def revenue_by_date(self):
        return self.transactions_bd.revenue()

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
        self.transactionsID = []
        self.count = 0
        self.revenue = 0
        self.unit_sold = 0
        self.transactions_bd = Transactions_bd()

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

class Transactions_bd:
    def __init__(self):
        self.transactions = {}

    def revenue(self):
        d = [[], []]
        for i in sorted(self.transactions.keys()):
            d[0].append(i)
            d[1].append(self.transactions[i])
        return d

    def unit_sold(self, records):
        d = [[], []]
        for i in sorted(self.transactions.keys()):
            d[0].append(i)
            d[1].append(transactions[i])
        return d

class Transactions(Plot):
    def __init__(self):
        # takes transaction id as key and record as value
        self.transactions = {}
        self.revenue = 0
        self.rating = 0
        self.stores = Store_locations()
        self.categories = Categories()
        self.payments = Payment_methods()
        self.header = []
        self.transactions_bd = Transactions_bd()

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

    def retrun_list_revenue(self):
        list = [[], []]
        for i in self.stores.store_locations.values():
            list[0].append(i.store_name)
            list[1].append(i.revenue)
        return list

    # Makes a pie chart using matplotlib as its base
    def pc_revenue_each_location(self):
        list = self.retrun_list_revenue()
        super().print_pie(list[0], list[1], "Pie chart of revenue contribution by store location.")

    # Makes a histogram using matplot lib as its base
    def hg_total_trans_value_el(self):
        list = [[], []]
        for i in self.stores.store_locations.values():
            list[0].append(i.store_name)
            list[1].append(len(i.transactionsID))
        super().print_hist(list, "Total transactions contribution by store location.", "Store Locations", "Number of Transactions")


    # Checks if the transaction id exists
    def print_t(self):
        while True:
            id = input("Enter the transactionId you are looking for: ")
            try:
                ui.printTransactions(self.transactions[id], self.header, 40)
                break
            except KeyError:
                print("Invalid ID.")
                option = input("Would you like to exit?(y/n) ").lower()
                if option == "y":
                    break

    # Prints the transactions of a store
    def print_ts(self):
        while True:
            name = input("Enter the Store name: ").strip().title()
            try:
                for i in self.stores.store_locations[name].transactionsID:
                    ui.printTransactions(self.transactions[i], self.header, 40)
                break
            except KeyError:
                print("Store doesn't exist: ")
                option = input("Would you like to exit?(y/n) ").lower()
                if option == "y":
                    break

    # Prints the transactions of a input category
    def print_tp(self):
        while True:
            name = input("Enter the product Category: ").strip().title()
            try:
                for i in self.categories.categories[name].transactionsID:
                    ui.printTransactions(self.transactions[i], self.header, 40)
                break
            except KeyError:
                print("Category doesn't exist: ")
                option = input("Would you like to exit?(y/n) ").lower()
                if option == "y":
                    break

    # Prints the revene of all teh stores
    def print_rs(self):
        list = []
        for i in self.stores.store_locations.keys():
            list.append([i, self.stores.store_locations[i].revenue])
        ui.print_header(["Store Location", "Revenue"], 40)
        ui.print_row(40, list, "-")

    # Prints the sales report of all the stores
    def print_srs(self):
        option = -1
        while option != "y":
            store = input("Enter the Store name: ").strip().title()
            try:
                print(self.stores.store_locations[store])
                break
            except KeyError:
                print("Store doesn't exist.")
                option = input("Would you like to exit?(y/n) ").lower().strip()
    def tbd_revenue_base(self, y):
        list = [[], []]
        x = y.revenue()
        for i in range(len(x[0])):
            list[0].append(x[0][i])
            list[1].append(sum([round(float(self.transactions[j][11]), 2) for j in x[1][i]]))

        return list

    def tbd_revenue(self, x):
        return self.tbd_revenue_base(self.transactions_bd)

    def return_tbd_all(self):
        list = []
        for i in self.stores.store_locations.values():
            list.append(self.tbd_revenue_base(i.transactions_bd))
            list[-1].append(i.store_name)
        return list