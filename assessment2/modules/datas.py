import csv
import os
import modules.ui
import modules.objects as obj

# Gets the path of current working dictionary
path = os.getcwd()

# Adds the information from row i to store_location
def add_to_store_location(store_locations, i):
    if i[2] not in store_locations.keys():
        store_locations[i[2]] = obj.Store(i[2])
    store_locations[i[2]].transactionsID.append(i[0])
    store_locations[i[2]].revenue = round(store_locations[i[2]].revenue+i[-1], 2)
    store_locations[i[2]].rating += i[-2]

# Adds the category information from row i to Categories
def add_to_categories(categories, i):
    if i[3] not in categories.keys():
        categories[i[3]] = obj.Category(i[3])
    categories[i[3]].count += 1
    categories[i[3]].unit_sold = round(categories[i[3]].unit_sold + i[6], 2)
    categories[i[3]].revenue = round(categories[i[3]].revenue + i[-1], 2)
    categories[i[3]].transactionsID.append(i[0])

# Adds the payment information from row i to Payment
def add_to_payment_methods(payment, i):
    if i[8] not in payment.keys():
        payment[i[8]] = obj.Payment(i[8])
    payment[i[8]].count += 1
    payment[i[8]].revenue = round(payment[i[8]].revenue + i[-1], 2)

# Fetches the data from csv files and returns dictionaries
def datas():
    with open(f"{path}/files/retail_sales_data.csv") as file:
        rows = csv.reader(file)
        header = next(rows)
        transactions = obj.Transactions()
        store_location = obj.Store_locations()
        category = obj.Categories()
        payment = obj.Payment_methods()

        for i in rows:
            i[-1], i[5], i[-2], i[6]= round(float(i[-1]), 2), int(i[5]), int(i[-2]), round(float(i[6]), 2)

            transactions.transactions[i[0]] = i
            transactions.revenue += i[-1]
            transactions.rating = i[-2]/5

            add_to_store_location(store_location.store_locations, i)

            # Adding data to store
            add_to_categories(store_location.store_locations[i[2]].categories.categories, i)
            add_to_payment_methods(store_location.store_locations[i[2]].payment_methods.methods, i)

            # Adding data to category
            add_to_categories(category.categories, i)

            # Adding data to payment method
            add_to_payment_methods(payment.methods, i)

        transactions.categories = category
        transactions.payments = payment
        transactions.stores = store_location

    return transactions, header


