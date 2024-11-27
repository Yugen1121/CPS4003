def printcolumn(list, var1):
    print("|", "=" * 28, "|")
    print(f"| {var1}", " "*(27-len(var1)), "|")
    print("|", "="*28, "|")
    rowLen = 27
    for i in list:
        print("| ", i, " "*(rowLen-len(i)-1),"|")
    print("|", "="*28, "|\n")