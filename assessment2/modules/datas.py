import csv
import os

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
        return transactions, store_location, category
