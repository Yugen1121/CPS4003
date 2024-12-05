from modules import datas
from modules import helpers as hel
from modules import ui
import matplotlib.pyplot as mp

menues = {1: """1. Retrieve the total number of transactions.
2. Retrieve unique store locations and product categories.
3. Retrieve details of a specific transaction using the TransactionID.
4. Retrieve all transactions for a specific store location.
5. Retrieve all transactions for a specific product category.
6. Group transactions by store location and calculate the total revenue per location.
7. Provide a summary of sales for a specific store location
8. Visualize The data
0. Exit"""}

def main():
    main, header = datas.datas()
    option = -1
    while option != 0:
        option = input("Enter the option\n"+menues[1]+"\n")
        option = hel.invalid_option(option, 8)
        if option == 1:
            print(f"The Total number of transaction is {len(main.transactions)}")

        elif option == 2:
            ui.printcolumn(main.stores.store_locations.keys(), "Store locations", 40)
            ui.printcolumn(main.categories.categories.keys(), "Categories", 40)

        elif option == 3:
            while True:
                id = input("Enter the transactionId you are looking for: ")
                try:
                    ui.printTransactions(main.transactions[id], header, 40)
                    break
                except KeyError:
                    print("Invalid ID.")
                    option = input("Would you like to exit?(y/n) ").lower()
                    if option == "y":
                        break

        elif option == 4:
            while True:
                name = input("Enter the Store name: ").strip().title()
                try:
                    for i in main.stores.store_locations[name].transactionsID:
                        ui.printTransactions(main.transactions[i], header, 40)
                    break
                except KeyError:
                    print("Store doesn't exist: ")
                    option = input("Would you like to exit?(y/n) ").lower()
                    if option == "y":
                        break

        elif option == 5:
            while True:
                name = input("Enter the product Category: ").strip().title()
                try:
                    for i in main.categories.categories[name].transactionsID:
                        ui.printTransactions(main.transactions[i], header, 40)
                    break
                except KeyError:
                    print("Category doesn't exist: ")
                    option = input("Would you like to exit?(y/n) ").lower()
                    if option == "y":
                        break

        elif option == 6:
            list = []
            for i in main.stores.store_locations.keys():
                list.append([i, main.stores.store_locations[i].revenue])
            ui.print_header(["Store Location", "Revenue"], 40)
            ui.print_row(40, list, "-")

        elif option == 7:
            x = datas.sales_report(transactions)
            payment_method = x[5]

            print(f"""
    SALES REPORT
    • Total transactions: {x[0]} 
    • Total revenue: {x[1]:.2f}
    • Average transaction value: {x[2]:.2f}
    • Total quantity of products sold: {x[3]:.2f}
    • Average customer satisfaction score: {x[4]:.2f}""")
            for i in payment_method.keys():
                print(f"\t-{i}: {payment_method[i]}%")
        elif option == 8:
            option = input("""1. Display a pie chart of revenue contribution by store location.
    2. Display a histogram of total transaction values.
    3. An interactive dashboard summarising key insights and trends and
    allowing further exploration of the data.
    0. Exit
    """)
            option = hel.invalid_option(option, 3)
            if option == 1:
                ui.print_pie(datas.total_revenue_per_location(transactions, store_location), "Pie chart of revenue contribution by store location.")
            elif option == 2:
                ui.print_hist(transactions, "Histogram of total transactions", "Total transaction", "Frequency of transaction amount")
            elif option == 3:
                ui.dashboard()
            elif option == 0:
                pass
        elif option == 0:
            print("Thank you!!")
            return True

if __name__ == "__main__":
    main()