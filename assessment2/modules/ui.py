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
    

    for i in list:
        print("| ", i, " "*(length-len(i)-2), end="")
    print("|")


def print_table_revenue(transaction, store, length):
    x = []
    print("|", "="*(length-2), "|", "="*(length-2), "|")
    print_row(length, [["Store Location", "Revenue"]], "=")
    for i in store.keys():
        x.append([i, sum([float(y) for y in [transaction[z][11] for z in [id for id in store[i]]]])])
    print_row(length, x, "-")