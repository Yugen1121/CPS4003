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

# class of graphs
class customGraph:
    def pie(self, list, title):
        fig, ax = plt.subplots(figsize=(5,5))
        ax.pie(list[1], labels = list[0], autopct='%1.1f%%')
        ax.set_title(title)
        return fig, ax


    def bar(self, list, title):
        leng = [i for i in range(len(list[1]))]
        fig, ax = plt.subplots(figsize=(5,6))
        ax.bar(leng, list[1])
        ax.set_xticks(leng)
        ax.set_xticklabels(list[0])
        ax.set_title(title)
        return fig, ax

    def random_rgb(self):
        return (random.random(), random.random(), random.random())

    def overlap_line(self, list, title):
        fig, ax = plt.subplots(figsize=(5,6))
        ax.tick_params(axis='x', rotation=90)
        for i in list:
            ax.plot(i[0], i[1], label = i[2], color=self.random_rgb())
        plt.legend(loc='upper right')
        ax.set_title(title)
        return fig, ax


# class for GUi
class Gui(customGraph):
    def __init__(self, main):
        self.main = main
        self.header = self.main.header
        self.window = tk.Tk()

    def new_frame(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        self.window.title("Dashboard")
        self.window.state('zoomed')
        self.window.configure(bg="black")

    def column_configure(self, x):
        for i in range(x):
            self.window.columnconfigure(i, weight=1)

    def label_configure(self):
        self.label = tk.Label(self.window)
        self.label.config(text="Dahsboard", font=("Helvetica", 20))
        self.label.grid(column=1, row=0, columnspan=2, sticky="ew")


    def run(self):
        self.new_frame()
        self.dashboard()
        self.window.update()
        self.window.mainloop()

    def print_revenue_location(self):
        list = [[], []]
        for i in self.main.stores.store_locations.values():
            list[0].append(i.store_name)
            list[1].append(i.revenue)
        return super().pie(list, "Ratio of revenue of each location")

    def print_transation_location(self):
        list = [[], []]
        for i in self.main.stores.store_locations.values():
            list[0].append(i.store_name)
            list[1].append(len(i.transactionsID))
        return super().bar(list, "Number of transactions done by each location.")

    def bar_revenue_bd(self):
        return super().bar(self.main.tbd_revenue(), "Revenue by date ")

    def all_rev_date(self):
        return super().overlap_line(self.main.return_tbd_revenue(), "Revenue of each location by date")

    def all_rev_c_date(self):
        return super().overlap_line(self.main.return_tbd_quantity(), "Unit sold of each location by date")




    def dashboard(self):
        # revenue location pie
        fig1, ax1 = self.print_revenue_location()

        # bar graph of number of transactions of each location
        fig2, ax2 = self.print_transation_location()

        # gives a scattered histogram of all the revenue by date of each location
        fig3, ax3 = self.all_rev_date()

        # gives a cattered histogram of all tge units sold by date of each location
        fig4, ax4 = self.all_rev_c_date()

        # adding the frames to the window
        frame = tk.Frame(self.window)
        frame.pack(fill="both", expand=True)

        canvas1 = FigureCanvasTkAgg(fig1, frame)
        canvas1.draw()
        canvas1.get_tk_widget().pack(side="left", fill="both", expand=True)

        canvas2 = FigureCanvasTkAgg(fig2, frame)
        canvas2.draw()
        canvas2.get_tk_widget().pack(side="left", fill="both", expand=True)

        canvas3 = FigureCanvasTkAgg(fig3, frame)
        canvas3.draw()
        canvas3.get_tk_widget().pack(side="left", fill="both", expand=True)

        canvas4 = FigureCanvasTkAgg(fig4, frame)
        canvas4.draw()
        canvas4.get_tk_widget().pack(side="left", fill="both", expand=True)