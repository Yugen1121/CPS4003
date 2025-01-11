import csv
import os
import modules.ui
import modules.objects as obj
import json

# Gets the path of current working dictionary
path = os.getcwd()

# Adds the information from row i to store_location
def add_to_store_location(store_locations, i):
    if i[2] not in store_locations.keys():
        store_locations[i[2]] = obj.Store(i[2])
    store_locations[i[2]].transactionsID.append(i[0])
    store_locations[i[2]].revenue = round(store_locations[i[2]].revenue+i[-1], 2)
    store_locations[i[2]].rating += i[-2]
    # Adding data to store categories
    add_to_categories(store_locations[i[2]].categories.categories, i)
    # Adding to store payment methods
    add_to_payment_methods(store_locations[i[2]].payment_methods.methods, i)
    # adding to store transactions_by_date
    add_to_transactions_bd(store_locations[i[2]].transactions_bd.transactions, i)

# Adds the category information from row i to Categories
def add_to_categories(categories, i):
    if i[3] not in categories.keys():
        categories[i[3]] = obj.Category(i[3])
    categories[i[3]].count += 1
    categories[i[3]].unit_sold = round(categories[i[3]].unit_sold + i[-1]/i[6], 2)
    categories[i[3]].revenue = round(categories[i[3]].revenue + i[-1], 2)
    categories[i[3]].transactionsID.append(i[0])
    add_to_transactions_bd(categories[i[3]].transactions_bd.transactions, i)

# Adds the payment information from row i to Payment
def add_to_payment_methods(payment, i):
    if i[8] not in payment.keys():
        payment[i[8]] = obj.Payment(i[8])
    payment[i[8]].count += 1
    payment[i[8]].revenue = round(payment[i[8]].revenue + i[-1], 2)
# adds the transactions by date
def add_to_transactions_bd(transactions, i):
    date = i[7][:7]
    if date not in transactions.keys():
        transactions[date] = []
    transactions[date].append(i[0])

# Fetches the data from csv files and returns dictionaries
def datas():
    with open(f"{path}/files/retail_sales_data.csv") as file:
        rows = csv.reader(file)
        header = next(rows)
        transactions = obj.Transactions()
        store_location = obj.Store_locations()
        category = obj.Categories()
        payment = obj.Payment_methods()
        tbd = obj.Transactions_bd()

        for i in rows:
            i[-1], i[5], i[-2], i[6]= round(float(i[-1]), 2), int(i[5]), int(i[-2]), round(float(i[6]), 2)

            transactions.transactions[i[0]] = i
            transactions.revenue += i[-1]
            transactions.rating = i[-2]

            # Adding datas to store locations
            add_to_store_location(store_location.store_locations, i)

            # Adding to the whole company transactions by date
            add_to_transactions_bd(tbd.transactions, i)

            # Adding data to category
            add_to_categories(category.categories, i)

            # Adding data to payment method
            add_to_payment_methods(payment.methods, i)

        transactions.categories = category
        transactions.payments = payment
        transactions.stores = store_location
        transactions.header = header
        transactions.rating = transactions.rating/len(transactions.transactions)
        transactions.transactions_bd = tbd
    return transactions

def json_exp(file):
    path = os.getcwd()+"\\json"
    print(f"Saving the file in '{path}'")
    with open(f"{path}\\{file["Loaction"]}.json", "w") as export:
        json.dump(file, export, indent=4)

