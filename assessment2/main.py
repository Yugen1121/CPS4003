from modules import datas
from modules import helpers as hel
from modules import ui

menues = {1: """1. Retrieve the total number of transactions.
2. Retrieve unique store locations and product categories.
3. Retrieve details of a specific transaction using the TransactionID.
4. Retrieve all transactions for a specific store location.
5. Retrieve all transactions for a specific product category.
6. Group transactions by store location and calculate the total revenue per location.
7. Provide a summary of sales for a specific store location
0. Exit"""}

def main():
    transactions, store_location, category, header = datas.datas()
    option = input("Enter the option\n"+menues[1])
    option = hel.invalid_option(option, 7)
    if option == 1:
        print(f"The Total number of transaction is {len(transactions)}")
    elif option == 2:
        ui.printcolumn(store_location.keys(), "Store locations", 40)
        ui.printcolumn(category.keys(), "Categories", 40)
    elif option == 3:
        while True:
            id = input("Enter the transactionId you are looking for: ")
            try:
                ui.printTransactions(transactions[id], header, 40)
                break
            except KeyError:
                print("Invalid ID.")
                option = input("Would you like to exit?(y/n) ").lower()
                if option == "y":
                    break
    elif option == 4:

        while True:
            name = input("Enter the Store name: ")
            try:
                for i in store_location[name]:
                    ui.printTransactions(transactions[i], header, 40)
                break
            except KeyError:
                print("Store doesn't exist: ")
                option = input("Would you like to exit?(y/n) ").lower()
                if option == "y":
                    break
    elif option == 5:
        while True:
            name = input("Enter the product Category: ")
            try:
                for i in category[name]:
                    ui.printTransactions(transactions[i], header, 40)
                break
            except KeyError:
                print("Category doesn't exist: ")
                option = input("Would you like to exit?(y/n) ").lower()
                if option == "y":
                    break

if __name__ == "__main__":
    main()