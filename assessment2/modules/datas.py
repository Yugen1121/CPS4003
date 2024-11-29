import csv
import os
import modules.ui

path = os.getcwd()


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
                category[row[3]].append(row[0])
            except KeyError:
                category[row[3]] = []
                category[row[3]].append(row[0])
        return transactions, store_location, category, header

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
