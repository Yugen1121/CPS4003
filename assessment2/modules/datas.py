import csv
import os
import modules.ui

# Gets the path of current working dictionary
path = os.getcwd()

class transactions:
    def __init__(self, dict):
        self.transactions = dict
        self.number_of_transaction = len(list)

class store_locations:
    def __init__(self, dict):
        self.store_locations = dict
        self.number_of_locations = len(dict.keys())

class categories:
    def __init__(self, dict):
        self.categories = dict
        self.number_of_categories = len(dict.keys())

# Fetches the data from csv files and returns dictionaries
def datas():
    with open(f"{path}/files/retail_sales_data.csv") as file:
        rows = csv.reader(file)
        header = next(rows)
        transactions = {}
        store_location = {}
        category = {}
        for row in rows:
            transactions[row[0]] = row
            try:
                store_location[row[2]].append(row[0])
            except KeyError:
                store_location[row[2]] = []
                store_location[row[2]].append(row[0])


            try:
                category[row[3]].append(row[0].lower())
            except KeyError:
                category[row[3]] = []
                category[row[3]].append(row[0].lower())

        # transactions uses transactionId as keys are the all the information as values
        # store_location takes store location as keys and transactionID as values
        # category takes category as keys and transactionID as values
        # header is a list that contains the headers
        return transactions, store_location, category, header

# returns the sales report
def sales_report(transactions):
    total_products_sold = 0
    total_transactions = len(transactions)
    total_revenue = 0
    total_customer_satisfaction = 0
    payment_methods = {}
    for i in transactions.values():
        total_products_sold += float(i[5])
        total_revenue += float(i[11])
        total_customer_satisfaction += float(i[10])
        try:
            payment_methods[i[8]] += 1
        except KeyError:
            payment_methods[i[8]] = 1

    for i in payment_methods.keys():
        payment_methods[i] = (float(payment_methods[i]) / float(total_transactions))*100

    total_customer_satisfaction = total_customer_satisfaction / total_transactions
    average_transaction_value = total_revenue / total_transactions

    return total_transactions, total_revenue, average_transaction_value,total_products_sold, total_customer_satisfaction, payment_methods

# returns total_revenue_per_location in a dic files where keys are the store location while the value are the total_revenue
def total_revenue_per_location(transactions, store_location):
    dic = {}
    for i in  store_location.keys():
        sum = 0
        for j in store_location[i]:
            sum += float(transactions[j][11])
        dic[i] = sum

    return dic