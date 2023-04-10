def get_total_price(data:str)->float:
    """
    This function returns the total price of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        float: fruits total price
    """
    ls = []
    f = open(data).read().split("\n")
    f.pop(0)
    f.pop(-1)
    for i in f:
        n = i.split(",")
        ls.append(float(n[1]))
    
    s = 0
    h = 0
    while s < len(ls):
        h += ls[s]
        s += 1
    return round(h,2)
print(get_total_price("fruits.csv"))

    