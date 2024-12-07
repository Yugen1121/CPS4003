import matplotlib.pyplot as plt
import tkinter as tk
import modules.datas as datas

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




def print_pie(labels, values, title):
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title(title)
    plt.show()

def print_hist(dictionary, title, xlabel,  ylabel):
    values = []
    for i in dictionary.values():
        values.append(float(i[11]))
    plt.hist(values)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def dashboard():
    window = tk.Tk()
    window.title("Dashboard")
    window.geometry("500x500")
    window.resizable(False, False)
    window.configure(bg="black")
    window.mainloop()