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
    main= datas.datas()
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
            main.print_t()

        elif option == 4:
            main.print_ts()

        elif option == 5:
            main.print_tp()

        elif option == 6:
            main.print_rs()

        elif option == 7:
            main.print_srs()
        elif option == 8:
            option = input("""1. Display a pie chart of revenue contribution by store location.
2. Display a histogram of total transaction values.
3. An interactive dashboard summarising key insights and trends and
allowing further exploration of the data.
0. Exit
    """)
            option = hel.invalid_option(option, 3)
            if option == 1:
                main.pc_revenue_each_location()
            elif option == 2:
                main.hg_total_trans_value_el()
            elif option == 3:
                x = ui.Gui(main, header)
                x.run()
            elif option == 0:
                pass
        elif option == 0:
            print("Thank you!!")
            return True

if __name__ == "__main__":
    main()