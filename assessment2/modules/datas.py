import csv
import os
import modules.ui
import modules.objects
from assessment2.modules.objects import transactions, Store_locations, Category, Payment, Payment_methods

# Gets the path of current working dictionary
path = os.getcwd()

# Fetches the data from csv files and returns dictionaries
def datas():
    with open(f"{path}/files/retail_sales_data.csv") as file:
        rows = csv.reader(file)
        header = next(rows)
        transactions = Transactions()
        store_location = Store_locations()
        category = Categories()
        payment = Payment_methods()

        for i in rows:
            transactions.transactions[i[0]] = i
            transactions.revenue += i[-1]
            transactions.rating += i[-2]/5

            if i[2] not in store_location.store_location.keys():
                store_location.store_location[i[2]] = Store(i[2])
            store_location.store_location[i[2]].transactionsID.append(i[0])
            store_location.store_location[i[2]].revenue = i[-1]
            store_location.store_location[i[2]].rating = i[-2]/5

            if i[3] not in store_location.store_location[1[2]].category[i[2]].keys():
                store_location.store_location[i[2]].categories[i[3]] = Category(i[3])
            store_location.store_location[i[2]].categories[i[3]].count += 1
            store_location.store_location[i[2]].categories[i[3]].unit_sold += i[6]
            store_location.store_location[i[2]].categories[i[3]].revenue += i[-1]

            if i[8] not in store_location.store_location[i[2]].payment_method.keys():
                store_location.store_location[i[2]].payment_method[i[8]] = Payment(i[8])
            store_location.store_location[i[2]].payment_method.count += 1
            store_location.store_location[i[2]].payment_method.revenue += i[-1]

            if i[3] not in category.category.keys():
                category.category[i[3]] = Category(i[3])
            category.category[i[3]].count += 1
            category.category[i[3]].unit_sold += i[6]
            category.category[i[3]].revenue += i[-1]

            if i[8] not in payment.method.keys():
                payment.method[i[8]] = Payment(i[8])
            payment.method[i[8]] += i[-1]
            payment.method[i[8]] += 1

        transactions.categories = category
        transactions.payments = payment
        transactions.stores = store_location
    return transactions

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