from modules import datas
from modules import helpers as hel
from modules import ui
import matplotlib.pyplot as mp
import sys

menues = {1: """1. Retrieve the total number of transactions.
2. Retrieve unique store locations and product categories.
3. Retrieve details of a specific transaction using the TransactionID.
4. Retrieve all transactions for a specific store location.
5. Retrieve all transactions for a specific product category.
6. Group transactions by store location and calculate the total revenue per location.
7. Provide a summary of sales for a specific store location
8. Visualize The data
9. Export json file
0. Exit"""}

def main():
    main= datas.datas()
    option = -1
    # The app runs while the option is not equal to 0
    while option != 0:
        # Asks the user for option and if invalid option asks again
        option = input("Enter the option\n"+menues[1]+"\n")
        option = hel.invalid_option(option, 9)

        # Option to see the total number of transaction
        if option == 1:
            print(f"The Total number of transaction is {len(main.transactions)}")

        # Option to see the unique store locations and categories
        elif option == 2:
            ui.printcolumn(main.stores.store_locations.keys(), "Store locations", 40)
            ui.printcolumn(main.categories.categories.keys(), "Categories", 40)

        # Option to check the transaction details by its ID
        elif option == 3:
            main.print_t_id()

        # Option to print all the transaction details by the store name
        elif option == 4:
            main.print_t_s()

        # Option to print all the transaction details by the category name
        elif option == 5:
            main.print_t_c()

        # Option to print the revenue of each store
        elif option == 6:
            main.print_rs()

        # Option to print the sales report of a specific store.
        elif option == 7:
            main.print_srs()

        # Option for charts and details
        elif option == 8:
            option1 = -1
            while option1 != 0:

                option1 = input("""1. Display a pie chart of revenue contribution by store location.
    2. Display a histogram of total transaction values.
    3. An interactive dashboard summarising key insights and trends and
    allowing further exploration of the data.
    0. Exit
        """)
                option1 = hel.invalid_option(option1, 3)
                # Shows a chart of revenue of each location
                if option1 == 1:
                    main.pc_revenue_each_location()

                # Shows the total transaction value
                elif option1 == 2:
                    main.hg_total_trans_value_el()
                # Opens a tkinter wind with multiple option in it
                elif option1 == 3:
                    x = ui.Gui(main)
                    x.run()

        # Option to make a json file report of a specific store
        elif option == 9:
            main.export()

        # Option to exit the application
        elif option == 0:
            print("Thank you!!")
            return True

if __name__ == "__main__":
    main()