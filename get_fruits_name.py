def get_frutis_name(data:str)->list:
    """
    This function returns the names of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        list: list of fruits names
    """
    ls = []
    f = open(data).read().split("\n")
    f.pop(0)
    f.pop(-1)
    for i in f:
        n = i.split(",")
        ls.append(n[0])
    return ls
print(get_frutis_name("fruits.csv"))

    