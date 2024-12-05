def invalid_option(option, ceil):
    try:
        option = int(option)
    except ValueError:
        option = -1
    while option < 0 or option > ceil:
        print("Invalid Option")
        try:
            option = int(input("Please choose the correct option: "))
        except TypeError:
            option = -1
    return option

def find_best(x, y):
    if x[1] > y[1]:
        return x
    return y

