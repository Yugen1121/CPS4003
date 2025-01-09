import modules.helpers
import matplotlib.pyplot as plt
import tkinter as tk
from modules.helpers import find_best
import modules.ui as ui
import modules.datas as hel

# a class to plot graphs
class Plot:

    # Function to create a pie char
    def print_pie(self, labels, values, title):
        plt.pie(values, labels=labels, autopct='%1.1f%%')
        plt.title(title)
        plt.show()

    # Function to create a histogram
    def print_hist(self, list, title, xlabel, ylabel):
        fig, ax = plt.subplots(1, 1)
        ax.hist(list, edgecolor = 'black')


        # Set title
        ax.set_title(title)

        # adding labels
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)

        # Make some labels.
        rects = ax.patches


            # Show plot
        plt.show()


# An atomic class that stores the data of specific paymetn method
class Payment:
    def __init__(self, method):
        # takes the input method and assigns it to method
        self.method = method
        self.revenue = 0
        self.count = 0

    def details(self):
        return {"Method": self.method,
                "Revenue": self.revenue,
                "Num of time uesd": self.count}
# A class derived from paymetnt that store all the different types paymetn method.
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

# An atomic class that stores the stat of a specific store
class Store:
    def __init__(self, location):
        self.store_name = location
        self.transactionsID = []
        self.revenue = 0
        self.rating = 0
        self.categories = Categories()
        self.payment_methods = Payment_methods()
        self.transactions_bd = Transactions_bd()

    # Returns the report of the store
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
• Average customer satisfaction score: {self.rating/len(self.transactionsID):.2f}\n""" + payments

    # Returns the details about the store
    def details(self):
        return {"Loaction": self.store_name,
                "Payment Methods": [i.details() for i in self.payment_methods.methods.values()],
                "Revenue" : self.revenue,
                "Total unit Sold": self.categories.total_unit(),
                "Rating": round(float(self.rating)/float(len(self.transactionsID)), 2),
                "Categories": [i.details() for i in self.categories.categories.values()],
                "TransactionID": self.transactionsID,
                "TransactionBD": self.transactions_bd.transactions}

    # Returns the most popular category
    def popular_category(self):
        return self.categories.popular()

    # Returns the category with the most revenue
    def most_revenue_category(self):
        return self.categories.most_revenue()

    # Returns all teh category soled in the store
    def all_categories(self):
        return self.categories.return_categories()

    # Returns all the revenue done in all the month
    def revenue_by_date(self):
        return self.transactions_bd.revenue()

# derived from the store class and holds all the unique stores locations
class Store_locations:
    def __init__(self):
        # takes store location as key and stores the store object as values
        self.store_locations = {}

    # returns all the details in (nested dictionary format [{}, {}]) of each stores to jsonify
    def details(self):
        x = []
        for i in self.store_locations.values():
            x.append(i.details())

        return x

# Stores all the detials of a unique category
class Category:
    def __init__(self, name):
        self.name = name
        self.transactionsID = []
        self.count = 0
        self.revenue = 0
        self.unit_sold = 0
        self.transactions_bd = Transactions_bd()

    def details(self):
        return {"Category": self.name,
                "Number of time bought": self.count,
                "Revenue": self.revenue,
                "Unit sold": self.unit_sold}
# Class that stores each category and uses methods to manipulate them
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
        for i in self.categories.values():
            sum += i.unit_sold
        return sum

# Stores all the transation done every date and uses the methods to return them
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
            d[1].append(self.transactions[i])
        return d

    def transaction(self):
        d = [[], []]
        for i in sorted(self.transactions.keys()):
            d[0].append(i)
            d[1].append(len(self.transactions[i]))
        return d

# The main class that stores everything about the super-market chain
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
        list = []
        for i in self.transactions.values():
            list.append(i[-1])
        super().print_hist(list, "Total transaction value", "Value", "Total transaction.")


    # Checks if the transaction id exists and prints the transaction detail
    def print_t_id(self):
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

    # Checks the store name and if valid prints all the transactions
    def print_t_s(self):
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

    # Chekcks if the category name is valid and if valid prints the transactions
    def print_t_c(self):
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

    # Prints the revene of each stores
    def print_rs(self):
        list = []
        for i in self.stores.store_locations.keys():
            list.append([i, self.stores.store_locations[i].revenue])
        ui.print_header(["Store Location", "Revenue"], 40)
        ui.print_row(40, list, "-")

    # Checks if the name of the given store is valid if it is valid prints the sales report.
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

    # Returns all the revenue by date in the list form
    def tbd_revenue_base(self, y):
        list = [[], []]
        x = y.revenue()
        for i in range(len(x[0])):
            list[0].append(x[0][i])
            list[1].append(sum([round(float(self.transactions[j][11]), 2) for j in x[1][i]]))

        return list

    # return all the transaction by date
    def tbd_revenue(self, x):
        return self.tbd_revenue_base(self.transactions_bd)

    # return revenue by date of each stores in the list format
    def return_tbd_revenue(self):
        list = []
        for i in self.stores.store_locations.values():
            list.append(self.tbd_revenue_base(i.transactions_bd))
            list[-1].append(i.store_name)
        return list

    # return the unit sold by date in list form
    def tbd_qunatity_base(self, y):
        list = [[], []]
        x = y.revenue()
        for i in range(len(x[0])):
            list[0].append(x[0][i])
            list[1].append(sum([round(float(self.transactions[j][5]), 2) for j in x[1][i]]))
        return list

    # return unit sold by date of each store
    def return_tbd_quantity(self):
        list = []
        for i in self.stores.store_locations.values():
            list.append(self.tbd_qunatity_base(i.transactions_bd))
            list[-1].append(i.store_name)
        return list

    def export(self):
        while True:
            store_name = input("Enter the store name: ").strip().title()
            try:
                hel.json_exp(self.stores.store_locations[store_name].details())
                break
            except KeyError:
                print("Invalid store name.")
                option = input("Would you like to exit?(y/n) ").lower()
                if option == "y":
                    break