import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math
import tkinter as tk
import modules.datas as datas
import modules.objects as obj
import random

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
    def __init__(self, main):
        self.main = main
        self.header = self.main.header
        self.window = tk.Tk()

    def new_frame(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        self.window.title("Dashboard")
        self.window.geometry("1000x700")
        self.window.resizable(False, False)
        self.window.configure(bg="black")

    def column_configure(self, x):
        for i in range(x):
            self.window.columnconfigure(i, weight=1)

    def label_configure(self):
        self.label = tk.Label(self.window)
        self.label.config(text="Dahsboard", font=("Helvetica", 20))
        self.label.grid(column=1, row=0, columnspan=2, sticky="ew")

    def click_button1(self):
        self.main.pc_revenue_each_location()

    def button_configure(self):
        self.button1 = tk.Button(self.window, text="Revenue percentage all location")
        self.button1.grid(column=1, row=1, columnspan=2, sticky="ew", padx=(5, 5), pady=(5, 5))
        self.button1.bind("<ButtonRelease-1>", lambda event: self.print_revenue_location())
        self.button2 = tk.Button(self.window, text="Histogram of units sold per location")
        self.button2.grid(column=1, row=2, columnspan=2, sticky="ew", padx=(5, 5), pady=(5, 5))
        self.button2.bind("<ButtonRelease-1>", lambda event: self.pie())
        self.button2.grid(column=1, row=2, columnspan=2, sticky="ew", padx=(5, 5), pady=(5, 5))
        self.button3 = tk.Button(self.window, text="Transactions by dates")
        self.button3.grid(column=1, row=3, columnspan=2, padx=(5, 5), pady=(5, 5))
        self.button3.bind("<ButtonRelease-1>", lambda event: self.all_rev_date())

    def run(self):
        self.new_frame()
        self.column_configure(4)
        self.label_configure()
        self.button_configure()
        self.window.update()
        self.window.mainloop()

    def print_revenue_location(self):
        list = [[], []]
        for i in self.main.stores.store_locations.values():
            list[0].append(i.store_name)
            list[1].append(i.revenue)
        self.pie(list)

    def bar_revenue_bd(self):
        self.bar(self.main.tbd_revenue())

    def all_rev_date(self):
        self.overlap_histogram(self.main.return_tbd_all())

    def pie(self, list):
        self.new_frame()
        fig, self.ax = plt.subplots(figsize=(5,5))
        self.ax.pie(list[1], labels = list[0], autopct='%1.1f%%')
        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.get_tk_widget().pack()
        quit_button = tk.Button(self.window, text="Menue")

        quit_button.bind("<ButtonRelease-1>", lambda event: self.run())
        quit_button.pack()
        self.window.update()
        self.window.mainloop()

    def bar(self, list):
        self.new_frame()
        fig, ax = plt.subplots(figsize=(5,6))
        ax.tick_params(axis='x', rotation=90)
        ax.bar(list[0], list[1])
        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.get_tk_widget().pack()
        quit_button = tk.Button(self.window, text="Menue")
        quit_button.bind("<ButtonRelease-1>", lambda event: self.run())
        quit_button.pack()
        self.window.update()
        self.window.mainloop()

    def random_rgb(self):
        return (random.random(), random.random(), random.random())

    def overlap_histogram(self, list):
        self.new_frame()
        fig, ax = plt.subplots(figsize=(5,7))
        ax.tick_params(axis='x', rotation=90)
        for i in list:
            ax.scatter(i[0], i[1], s=50, label = i[2], color=self.random_rgb())
        plt.legend(loc='upper right')
        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.get_tk_widget().pack()
        quit_button = tk.Button(self.window, text="Menue")
        quit_button.bind("<ButtonRelease-1>", lambda event: self.run())
        quit_button.pack()
        self.window.update()
        self.window.mainloop()