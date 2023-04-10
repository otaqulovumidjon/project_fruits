def get_cheapest_fruit(data: str) -> str:
    """
    This function returns the name of the cheapest fruit

    args:
        data: CSV file with the fruits data
    returns:
        str: name of the cheapest fruit
    """
    js = []
    ls = []
    f = open(data).read().split("\n")
    f.pop(0)
    f.pop(-1)
    for i in f:
        n = i.split(",")
        js.append(float(n[1]))
        ls.append(n[0])
    
    x = 0
    y = 0
    while x < len(js):
        if y < js[x]:
            y = js[x]
        x += 1

    z = 0
    while z < len(js):
        if y > js[z]:
            y = js[z]
        z += 1
    l = js.index(y)
    return ls[l]
print(get_cheapest_fruit("fruits.csv"))

    # your code here