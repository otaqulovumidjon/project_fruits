def get_cheapest_fruit_id(data: str) -> int:
    """
    This function returns the index of the cheapest fruit

    args:
        data (str): CSV file with the fruits data
    returns:
        int: id of the cheapest fruit
    """
    js = []

    f = open(data).read()
    n = f.split("\n")
    n.pop(0)
    n.pop(-1)
    l = n
    for i in l:
        s = i.split(",")
        js.append(float(s[1]))

    x = 0
    y = 0
    while x < len(js):
        if js[x] > y:
            y = js[x]
        x += 1

    b = 0
    c = 0
    while b < len(js):
        if js[b] < y:
            y = js[b]
        b += 1
    # return y
    return js.index(y)
print(get_cheapest_fruit_id("fruits.csv"))
    # your code here