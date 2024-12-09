import matplotlib.pyplot as plt
import tkinter as tk
import modules.datas as datas
import modules.objects as obj


# Function to print a column
def printcolumn(list, var1, length):
    print("|", "=" * length, "|")
    print(f"| {var1}", " "*(length-len(var1)-1), "|")
    print("|", "="*length, "|")
    for i in list:
        print("| ", i, " "*(length-len(i)-2),"|")
    print("|", "="*length, "|\n")

def printTransactions(list, header, length):
    
    print("|", "=" * length, "|")
    for i in range(len(header)):
        x = f"{header[i]}: {list[i]}"
        print("| ", x, " "*(length-2-len(x)), "|")
    print("|", "="*length, "|\n")

def print_row(length, values, sign):
    for value in values:
        for i in range(len(value)):
            print("| ", value[i], " "*(length-3-len(str(value[i]))), end="")
        print("|")

    for i in range(len(values[0])):
        print("|", f"{sign}"*(length-1), end="")
    print("|")

def print_header(list, length):
    for i in list:
        print("|", "="*(length-1), end="")
    print("|")
    for i in list:
        print("| ", i, " "*(length-len(i)-3), end="")
    print("|")
    for i in list:
        print("|", "="*(length-1), end="")
    print("|")

class Gui:
    def __init__(self, main, header):
        self.main = main
        self.header = header
        self.window = tk.Tk()
        self.window.title("Dashboard")
        self.window.geometry("500x500")
        self.window.resizable(False, False)
        self.window.configure(bg="black")

    def column_configure(self, x):
        for i in range(x):
            self.window.columnconfigure(i, weight=1)

    def label_configure(self):
        self.label = tk.Label(self.window)
        self.label.config(text="Dahsboard", font=("Helvetica", 20))
        self.label.grid(column=1, row=0, columnspan=2, sticky="ew")

    def click_button1(self, event=None):
        self.main.pc_revenue_each_location()

    def click_button2(self, event=None):
        self.main.hg_total_trans_value_el()
    def button_configure(self):
        self.button1 = tk.Button(self.window, text="Revenue percentage all location")
        self.button1.grid(column=1, row=1, columnspan=2, sticky="ew", padx=(5, 5), pady=(5, 5))
        self.button1.bind("<ButtonRelease-1>", self.click_button1)
        self.button2 = tk.Button(self.window, text="Histogram of units sold per location")
        self.button2.grid(column=1, row=2, columnspan=2, sticky="ew", padx=(5, 5), pady=(5, 5))
        self.button2.bind("<ButtonRelease-1>", self.click_button2)

    def run(self):
        self.column_configure(4)
        self.label_configure()
        self.button_configure()
        self.window.mainloop()
