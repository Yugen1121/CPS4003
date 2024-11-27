from modules import datas
from modules import ui


def main():
    transactions, store_location, category, header = datas.datas()
    ui.printcolumn(store_location, "Store Location")
    ui.printcolumn(category, "Categories")
    pass

if __name__ == "__main__":
    main()