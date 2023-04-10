def get_expensive_fruit(data: str) -> str:
    """
    This function returns the name of the most expensive fruit

    args:
        data: CSV file with the fruits data
    returns:
        str: name of the most expensive fruit
    """
    ls = []
    js = []
    f = open(data).read().split("\n")
    f.pop(0)
    f.pop(-1)
    for i in f:
        n = i.split(",")
        ls.append(float(n[1]))
        js.append(n[0])

    x = 0
    y = 0
    while x < len(ls):
        if y < ls[x]:
            y = ls[x]
        x += 1
    l = ls.index(y)
    return js[l]
print(get_expensive_fruit("fruits.csv"))

    # your code here