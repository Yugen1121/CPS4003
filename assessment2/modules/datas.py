import csv
import os

path = os.getcwd()

def datas():
    with open(f"{path}/files/retail_sales_data.csv") as file:
        rows = csv.reader(file)
        headers = rows
        transactions = {}
        store_location = {}
        category = {}
        for row in rows:
            transactions[row[0]] = row
            try:
                store_location[row[2]].append(row[0])
            except KeyError:
                store_location[row[2]] = []
                store_location.append[row[2]]
             
            try:
                category[row[3]].append(row[0])
            except KeyError:
                category[row[3]] = []
                category.append[row[2]]
        return (transactions, store_location, category)
